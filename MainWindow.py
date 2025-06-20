
import copy
import datetime
import math
import os
import random
import re
import sys
from PySide2.QtWidgets import QMainWindow, QMessageBox, QApplication
from PySide2.QtCore import QTimer, Qt, QDateTime, Signal, QUrl, QRect, QPoint
from PySide2.QtGui import QIcon, QPen, QGuiApplication, QFont, QColor, QPixmap, QPainter
from PySide2.QtMultimedia import QMediaPlayer, QMediaContent

import serial
from CK_Dialog import CK_Dialog
from Info_Dialog import Info_Dialog
from BJ_Dialog import BJ_Dialog
from Load_Dialog import Load_Dialog
from PackUnpack import PackUnpack
from ui_MainWindow import Ui_ECGB_Window

class MainWindow(QMainWindow, Ui_ECGB_Window):
    THRESHOLD_SIGNAL = Signal(int, int, int, int, int, int, int)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
        self.setWindowTitle('ECGB')
        self.setFixedSize(1200, 900)

        self.CK_Dialog = CK_Dialog()
        self.CK_Dialog.setWindowTitle('串口设置')
        self.CK_Dialog.setWindowModality(Qt.ApplicationModal) 
        self.CK_Dialog.hide()
        self.CK_Dialog.serialSignal.connect(self.serial_slot)

        self.Info_Dialog = Info_Dialog()
        self.Info_Dialog.setWindowTitle('信息设置')
        self.Info_Dialog.setWindowModality(Qt.ApplicationModal)
        self.Info_Dialog.setSignal.connect(self.text_slot)

        self.BJ_Dialog = BJ_Dialog()
        self.BJ_Dialog.setWindowTitle('阈值设置')
        self.BJ_Dialog.setWindowModality(Qt.ApplicationModal)
        self.BJ_Dialog.thresholdSignal.connect(self.threshold_slot)

        self.Load_Dialog = Load_Dialog()
        self.Load_Dialog.setWindowTitle('数据导入')
        self.Load_Dialog.setWindowModality(Qt.ApplicationModal)
        self.Load_Dialog.setSignal.connect(self.load_slot)
        self.config()

    def config(self):
        self.CK_btn.clicked.connect(self.CK_slot)
        self.XX_btn.clicked.connect(self.Info_Dialog.show)
        self.JC_btn.clicked.connect(self.JC_slot)
        self.BJ_btn.clicked.connect(self.BJ_Dialog.show)
        self.SJ_btn.clicked.connect(self.SJ_slot)
        self.load_btn.clicked.connect(self.Load_Dialog.show)

        self.THRESHOLD_SIGNAL.connect(self.BJ_Dialog.threshold_slot)

        self.ser = serial.Serial()
        self.mPackUnpck = PackUnpack()
        self.time_list = []

        # ECG
        self.mECG1WaveList = [] 
        self.mEcgXStep = 0 
        self.maxEcgLength = self.ECG_wave.width()
        self.maxEcgHeight = self.ECG_wave.height()
        self.pixmapEcg = QPixmap(self.ECG_wave.width(), self.ECG_wave.height())
        self.pixmapEcg.fill(Qt.black)
        self.ECG_wave.setPixmap(self.pixmapEcg)
        self.painterEcg = QPainter(self.pixmapEcg)

        # Resp
        self.mRESPWaveList = [] 
        self.mRespXStep = 0
        self.maxRespLength = self.RESP_wave.width()
        self.maxRespHeight = self.RESP_wave.height() 
        self.pixmapResp = QPixmap(self.RESP_wave.width(), self.RESP_wave.height())
        self.pixmapResp.fill(Qt.black)
        self.RESP_wave.setPixmap(self.pixmapResp)
        self.painterResp = QPainter(self.pixmapResp)

        # SPO2
        self.mSPO2WaveList = [] 
        self.mSpo2XStep = 0
        self.maxSpo2Length = self.SPO2_wave.width() 
        self.maxSpo2Height = self.SPO2_wave.height()
        self.pixmapSpo2 = QPixmap(self.SPO2_wave.width(), self.SPO2_wave.height())
        self.pixmapSpo2.fill(Qt.black) 
        self.SPO2_wave.setPixmap(self.pixmapSpo2)
        self.painterSpo2 = QPainter(self.pixmapSpo2)

        # 时间更新定时器
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        self.serialPortTimer = QTimer(self)
        self.serialPortTimer.timeout.connect(self.data_receive)

        self.procDataTimer = QTimer(self)
        self.procDataTimer.timeout.connect(self.data_process)

        self.simulateTimer = QTimer(self)
        self.simulateTimer.timeout.connect(self.receive_simulate_data)

        self.updateTimer = QTimer(self)
        self.updateTimer.setInterval(1000)
        self.updateTimer.timeout.connect(self.update_hr_display)
        self.updateTimer.timeout.connect(self.update_resp_display)
        self.updateTimer.timeout.connect(self.update_spo2_display)
        self.updateTimer.timeout.connect(self.update_pr_display)

        self.alarm_player = QMediaPlayer()
        self.alarm_player.setMedia(QMediaContent(QUrl.fromLocalFile('alarm.mp3')))
        self.is_alarming = False

        self.HR_threshold_low = 60
        self.HR_threshold_high = 100
        self.RESP_threshold_low = 12
        self.RESP_threshold_high = 24
        self.SPO2_threshold_low = 94
        self.PR_threshold_low = 60
        self.PR_threshold_high = 500
        self.maxPoints = 300

        self.current_hr = 0
        self.current_resp = 0
        self.current_spo2 = 0
        self.current_pr = 0

        self.HR_blink_state = False
        self.RESP_blink_state = False
        self.SPO2_blink_state = False
        self.PR_blink_state = False

        self.mPackAfterUnpackArr = []
        self.saveDataPath = ""
        self.limit = 0

    def CK_slot(self):
        self.clear_all()
        if self.name_label.text() != "None":
            self.CK_Dialog.show()
        else:
            QMessageBox.critical(self, "Error", "请先填写信息！")
            return
    
    def serial_slot(self, portNum, baudRate, dataBits, stopBits, parity):
        if self.ser.isOpen():
            self.serialPortTimer.stop()
            self.procDataTimer.stop()
            self.updateTimer.stop()
            try:
                self.ser.close()
            except:
                pass
            self.status_label.setText("串口已关闭")
            self.status_label.setStyleSheet("color: #ff0000")
            self.CK_Dialog.Open_btn.setText("打开串口")
            self.CK_Dialog.hide()
            return
        
        self.ser.port = portNum
        self.ser.baudrate = int(baudRate)
        self.ser.bytesize = int(dataBits)
        self.ser.stopbits = int(stopBits)
        self.ser.parity = parity
        try:
            self.ser.open()
        except:
            QMessageBox.critical(self, "Error", "串口打开失败")
            return

        self.serialPortTimer.start(2)
        self.procDataTimer.start(10)
        self.updateTimer.start()

        self.status_label.setText("串口已打开")
        self.status_label.setStyleSheet("color: #ffffff")
        self.CK_Dialog.Open_btn.setText("关闭串口")
        self.CK_Dialog.hide()
    
    # 处理串口接收的数据
    def data_receive(self):
        try:
            num = self.ser.inWaiting()  # 获取当前串口缓冲区的数据量
        except:
            self.serialPortTimer.stop()
            self.procDataTimer.stop()
            try:
                self.ser.close()
            except:
                pass
            return None
        if num > 0:
            data = self.ser.read(num)  # 读取当前串口缓冲区的数据
            # 通过for循环遍历data中的数据，直到获取一个完整的数据包时，findPack才为True
            for i in range(0, len(data)):
                findPack = self.mPackUnpck.unpackData(data[i])
                # 解包成功，将数据保存到mPackAfterUnpackArr列表中
                if findPack:
                    temp = self.mPackUnpck.getUnpackRslt()
                    self.mPackAfterUnpackArr.append(copy.deepcopy(temp))
        else:
            pass

    # 处理已解包的数据
    def data_process(self):
        num = len(self.mPackAfterUnpackArr)
        if num > 0:
            for i in range(num):
                if self.mPackAfterUnpackArr[i][0] == 0x10:
                    self.analyzeECGData(self.mPackAfterUnpackArr[i])
                if self.mPackAfterUnpackArr[i][0] == 0x11:
                    self.analyzeRESPData(self.mPackAfterUnpackArr[i])
                if self.mPackAfterUnpackArr[i][0] == 0x13:
                    self.analyzeSPO2Data(self.mPackAfterUnpackArr[i])
                # 保存数据
                if self.saveDataPath:
                    if self.limit < 4460:
                        with open(self.saveDataPath, 'a') as file:
                            data = []
                            for j in range(0, 8):
                                data.append(self.mPackAfterUnpackArr[i][j])
                            file.write(str(data) + '\n')
                            self.limit += 1
                    else:
                        self.saveDataPath = ""
                        self.limit = 0
            del self.mPackAfterUnpackArr[0:num]

        if len(self.mECG1WaveList) > 2:
            self.drawECGWave()
        if len(self.mRESPWaveList) > 2:
            self.drawRESPWave()
        if len(self.mSPO2WaveList) > 2:
            self.drawSPO2Wave()

    def analyzeECGData(self, data):
        if data[1] == 0x02:
            ecgData1 = data[2] << 8 | data[3]
            self.mECG1WaveList.append(ecgData1)
        elif data[1] == 0x03:
            if data[2] == 1:
                self.DL1_label.setStyleSheet("color:red")
            else:
                self.DL1_label.setStyleSheet("color:green")
        elif data[1] == 0x04:
            self.current_hr = data[2] << 8 | data[3]
            self.update_hr_display()

    def analyzeRESPData(self, data):
        if data[1] == 0x02:
            resp = data[2] << 8 | data[3]
            self.mRESPWaveList.append(resp)
        elif data[1] == 0x03:
            self.current_resp = data[2] << 8 | data[3]
            self.update_resp_display()
        elif data[1] == 0x06:
            if data[2] == 1:
                self.DL2_label.setStyleSheet("color:green")
            else:
                self.DL2_label.setStyleSheet("color:red")

    def analyzeSPO2Data(self, data):
        if data[1] == 0x02:
            spo2Data = data[2] << 8 | data[3]
            if spo2Data != 0:
                self.mSPO2WaveList.append(spo2Data)
        elif data[1] == 0x04:
            if data[2] == 0x01:
                self.DL3_label.setText("手指脱落")
                self.DL3_label.setStyleSheet("color:red")
            else:
                self.DL3_label.setStyleSheet("color:black")
        elif data[1] == 0x05:
            if data[2] == 0x01:
                self.DL4_label.setText("探头脱落")
                self.DL4_label.setStyleSheet("color:red")
            else:
                self.DL4_label.setStyleSheet("color:black")
        elif data[1] == 0x03:
            self.current_spo2 = data[3]
            self.update_spo2_display()
        elif data[1] == 0x06:
            self.current_pr = data[2]
            self.update_pr_display()

    def drawECGWave(self):
        iCnt = len(self.mECG1WaveList)

        self.painterEcg.setBrush(Qt.black)
        self.painterEcg.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        if iCnt > self.maxEcgLength - self.mEcgXStep:
            ECG1Rect = QRect(self.mEcgXStep, 0, self.maxEcgLength - self.mEcgXStep, self.maxEcgHeight)
            ECG2Rect = QRect(0, 0, 10 + iCnt - (self.maxEcgLength - self.mEcgXStep), self.maxEcgHeight)
            self.painterEcg.drawRect(ECG1Rect)
            self.painterEcg.drawRect(ECG2Rect)
        else:
            self.painterEcg.drawRect(QRect(self.mEcgXStep, 0, iCnt + 10, self.maxEcgHeight))

        pen = QPen(QColor("#00ff00"), 4, Qt.SolidLine)
        self.painterEcg.setPen(pen)

        for i in range(iCnt - 1):
            # y1 = int(self.maxEcgHeight / 2 - (self.mECG1WaveList[i] - 2048) / 3)
            # y2 = int(self.maxEcgHeight / 2 - (self.mECG1WaveList[i + 1] - 2048) / 3)
            y1 = int(self.maxEcgHeight / 2 - (self.mECG1WaveList[i] - 2048) / 15)
            y2 = int(self.maxEcgHeight / 2 - (self.mECG1WaveList[i + 1] - 2048) / 15)
            x1 = self.mEcgXStep
            x2 = self.mEcgXStep + 1

            self.painterEcg.drawLine(QPoint(x1, y1), QPoint(x2, y2))

            self.mEcgXStep += 1
            if self.mEcgXStep > self.maxEcgLength:
                self.mEcgXStep = 0

        self.mECG1WaveList = self.mECG1WaveList[-1:]
        self.ECG_wave.setPixmap(self.pixmapEcg)

    
    def drawRESPWave(self):
        iCnt = len(self.mRESPWaveList)
        self.painterResp.setBrush(Qt.black)
        self.painterResp.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        if iCnt > self.maxRespLength - self.mRespXStep:
            RESP1Rect = QRect(self.mRespXStep, 0, self.maxRespLength - self.mRespXStep, self.maxRespHeight)
            RESP2Rect = QRect(0, 0, 10 + iCnt - (self.maxRespLength - self.mRespXStep), self.maxRespHeight)
            self.painterResp.drawRect(RESP1Rect)
            self.painterResp.drawRect(RESP2Rect)
        else:
            self.painterResp.drawRect(QRect(self.mRespXStep, 0, iCnt + 10, self.maxRespHeight))

        pen = QPen(QColor("#ffb300"), 4, Qt.SolidLine)
        self.painterResp.setPen(pen)

        for i in range(iCnt - 1):
            # y1 = int(self.maxRespHeight - self.mRESPWaveList[i] / 20)
            # y2 = int(self.maxRespHeight - self.mRESPWaveList[i+1] / 20)
            y1 = int((self.maxRespHeight - (self.mRESPWaveList[i] - 14000) * 0.005))
            y2 = int((self.maxRespHeight - (self.mRESPWaveList[i+1] - 14000) * 0.005))
            x1 = self.mRespXStep
            x2 = self.mRespXStep + 1

            self.painterResp.drawLine(QPoint(x1, y1), QPoint(x2, y2))

            self.mRespXStep += 1
            if self.mRespXStep > self.maxRespLength:
                self.mRespXStep = 0

        self.mRESPWaveList = self.mRESPWaveList[-1:]
        self.RESP_wave.setPixmap(self.pixmapResp)
    
    def drawSPO2Wave(self):
        iCnt = len(self.mSPO2WaveList)

        self.painterSpo2.setBrush(Qt.black)
        self.painterSpo2.setPen(QPen(Qt.black, 2, Qt.SolidLine))

        if iCnt > self.maxSpo2Length - self.mSpo2XStep:
            SPO21Rect = QRect(self.mSpo2XStep, 0, self.maxSpo2Length - self.mSpo2XStep, self.maxSpo2Height)
            SPO22Rect = QRect(0, 0, 10 + iCnt - (self.maxSpo2Length - self.mSpo2XStep), self.maxSpo2Height)
            self.painterSpo2.drawRect(SPO21Rect)
            self.painterSpo2.drawRect(SPO22Rect)
        else:
            self.painterSpo2.drawRect(QRect(self.mSpo2XStep, 0, iCnt + 10, self.maxSpo2Height))

        pen = QPen(QColor("#00ffee"), 4, Qt.SolidLine)
        self.painterSpo2.setPen(pen)

        for i in range(iCnt - 1):
            # y1 = int((self.maxSpo2Height - (self.mSPO2WaveList[i]) / 10))
            # y2 = int((self.maxSpo2Height - (self.mSPO2WaveList[i + 1]) / 10))
            y1 = int((self.maxSpo2Height - self.mSPO2WaveList[i]) / 5)
            y2 = int((self.maxSpo2Height - self.mSPO2WaveList[i + 1]) / 5)
            x1 = self.mSpo2XStep
            x2 = self.mSpo2XStep + 1

            self.painterSpo2.drawLine(QPoint(x1, y1), QPoint(x2, y2))

            self.mSpo2XStep += 1
            if self.mSpo2XStep > self.maxSpo2Length:
                self.mSpo2XStep = 0

        self.mSPO2WaveList = self.mSPO2WaveList[-1:]
        self.SPO2_wave.setPixmap(self.pixmapSpo2)


    def update_hr_display(self):
        """更新心率显示标签"""
        if self.current_hr < 300:
            self.HR_label.setText(f"{self.current_hr}")
            if self.current_hr > 0 and (self.current_hr < self.HR_threshold_low or self.current_hr > self.HR_threshold_high):
                if not self.is_alarming:
                    self.alarm_player.play()
                    self.is_alarming = True

                if self.alarm_player.state() != QMediaPlayer.PlayingState:
                    self.alarm_player.play()

                if self.HR_blink_state:
                    self.HR_label.setFont(QFont("Agency FB", 120))
                    self.HR_label.setStyleSheet("color: #ff0000")
                    if self.current_hr > self.HR_threshold_high:  # 高心率闪烁
                        self.state_label.setText("心率过速")
                        self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #00ff00")
                    elif self.current_hr < self.HR_threshold_low:
                        self.state_label.setText("心率过缓")
                        self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #00ff00")
                else:
                    self.HR_label.setFont(QFont("Agency FB", 130))

                self.HR_blink_state = not self.HR_blink_state
            else:
                if "background-color: #00ff00" in self.state_label.styleSheet():
                    self.state_label.setText("正常")
                    self.state_label.setStyleSheet("color: #00ff00")
                if self.is_alarming:
                    self.alarm_player.stop()
                    self.is_alarming = False

                self.HR_label.setFont(QFont("Agency FB", 120))
                self.HR_label.setStyleSheet("color: #00ff00")  # 绿色
                self.HR_blink_state = False  # 重置闪烁状态

    def update_resp_display(self):
        """更新呼吸率显示标签"""
        if self.current_resp < 30:
            self.RESP_label.setText(f"{self.current_resp}")
            if self.current_resp > 0 and (self.current_resp < self.RESP_threshold_low or self.current_resp > self.RESP_threshold_high):
                if not self.is_alarming:
                    self.alarm_player.play()
                    self.is_alarming = True

                if self.alarm_player.state() != QMediaPlayer.PlayingState:
                    self.alarm_player.play()

                if self.RESP_blink_state:
                    self.RESP_label.setFont(QFont("Agency FB", 120))
                    self.RESP_label.setStyleSheet("color: #ff0000")
                    if self.current_resp > self.RESP_threshold_high:
                        self.state_label.setText("呼吸过快")
                        self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #ffc300")
                    elif self.current_resp < self.RESP_threshold_low:
                        self.state_label.setText("呼吸过慢")
                        self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #ffc300")
                else:
                    self.RESP_label.setFont(QFont("Agency FB", 130))

                self.RESP_blink_state = not self.RESP_blink_state
            else:
                if "background-color: #ffc300" in self.state_label.styleSheet():
                    self.state_label.setText("正常")
                    self.state_label.setStyleSheet("color: #00ff00")
                if self.is_alarming:
                    self.alarm_player.stop()
                    self.is_alarming = False

                self.RESP_label.setFont(QFont("Agency FB", 120))
                self.RESP_label.setStyleSheet("color: #ffc300")
                self.RESP_blink_state = False  # 重置闪烁状态

    def update_spo2_display(self):
        """更新血氧显示标签"""
        self.SpO2_label.setText(f"{self.current_spo2}")
        if self.current_spo2 > 0 and self.current_spo2 < self.SPO2_threshold_low:
            if not self.is_alarming:
                self.alarm_player.play()
                self.is_alarming = True

            if self.alarm_player.state() != QMediaPlayer.PlayingState:
                self.alarm_player.play()

            if self.SPO2_blink_state:
                self.SpO2_label.setStyleSheet("color: #ff0000")
                self.state_label.setText("血氧饱和度过低")
                self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #00ffee")
            else:
                self.SpO2_label.setFont(QFont("Agency FB", 90))

            self.SPO2_blink_state = not self.SPO2_blink_state

        else:
            if "background-color: #00ffee" in self.state_label.styleSheet():
                self.state_label.setText("正常")
                self.state_label.setStyleSheet("color: #00ff00")

            if self.is_alarming:
                self.alarm_player.stop()
                self.is_alarming = False

            self.SpO2_label.setFont(QFont("Agency FB", 80))
            self.SpO2_label.setStyleSheet("color: #00ffee")
            self.SPO2_blink_state = False

    def update_pr_display(self):
        """更新脉率显示标签"""
        self.PR_label.setText(f"{self.current_pr}")
        if self.current_pr > 0 and (self.current_pr < self.PR_threshold_low or self.current_pr > self.PR_threshold_high):
            if not self.is_alarming:
                self.alarm_player.play()
                self.is_alarming = True

            if self.alarm_player.state() != QMediaPlayer.PlayingState:
                self.alarm_player.play()

            if self.PR_blink_state:
                self.PR_label.setFont(QFont("Agency FB", 80))
                self.PR_label.setStyleSheet("color: #ff0000")
                if self.current_pr > self.PR_threshold_high:
                    self.state_label.setText("脉率过高")
                    self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #11ffee")
                elif self.current_pr < self.PR_threshold_low:
                    self.state_label.setText("脉率过低")
                    self.state_label.setStyleSheet("border-radius: 5px; color: #000000; background-color: #11ffee")
            else:
                self.PR_label.setFont(QFont("Agency FB", 90))

            self.PR_blink_state = not self.PR_blink_state

        else:
            if "background-color: #11ffee" in self.state_label.styleSheet():
                self.state_label.setText("正常")
                self.state_label.setStyleSheet("color: #00ff00")
            if self.is_alarming:
                self.alarm_player.stop()
                self.is_alarming = False

            self.PR_label.setFont(QFont("Agency FB", 80))
            self.PR_label.setStyleSheet("color: #00ffee")
            self.PR_blink_state = False

    def SJ_slot(self, path):
        if self.name_label.text() != "None":
            name = self.name_label.text()
            sex = "m" if self.sex_label.text() == "男" else "f"
            mode = self.Info_Dialog.comboBox_2.currentIndex()
            time_label = self.date_label.text() + "_" + self.time_label.text()
            time_label = time_label.replace(":", "-")

            self.filepath = os.getcwd() + rf"\Data\{name}_{sex}_{mode}_{time_label}.txt"
            self.saveDataPath = self.filepath
            QMessageBox.information(self, "提示", f"数据保存至{self.filepath}", QMessageBox.Yes)
        else:
            QMessageBox.warning(self, "警告", "请先输入患者信息！", QMessageBox.Yes)
            return

    def load_slot(self, path):
        basename = os.path.basename(path)

        # 检查文件名是否符合标准
        if re.match(r"^[\u4e00-\u9fa5a-zA-Z0-9_]+_[mf]_[0-9]+_[0-9]{4}-[0-9]{2}-[0-9]{2}_[0-9]{2}-[0-9]{2}-[0-9]{2}\.txt$", basename):
            name = basename.split("_")[0]
            sex = basename.split("_")[1]
            mode = int(basename.split("_")[2])
            
            if mode == 0:
                mode_name = "成人"
            elif mode == 1:
                mode_name = "新生儿"
            elif mode == 2:
                mode_name = "婴儿"
            elif mode == 3:
                mode_name = "幼儿"
            elif mode == 4:
                mode_name = "学龄前"
            elif mode == 5:
                mode_name = "学龄"
            elif mode == 6:
                mode_name = "青少年"
            else:
                mode_name = "其他"

            self.name_label.setText(name)
            self.sex_label.setText("男" if sex == "m" else "女")
            self.mode_label.setText(mode_name)

        self.SPO2_wave.setPixmap(self.pixmapSpo2)
        self.ECG_wave.setPixmap(self.pixmapEcg)
        self.RESP_wave.setPixmap(self.pixmapResp)

        self.data_file = open(path, "rb")
        self.simulateTimer.start(2)
        self.status_label.setText("数据模拟中")
        self.procDataTimer.start(10)
        self.updateTimer.start()
    
    def receive_simulate_data(self):
        data = self.data_file.readline()
        if data:
            data_list = eval(data.strip())
            byte_data = bytes(data_list)
            self.mPackAfterUnpackArr.append(byte_data)
        else:
            QMessageBox.information(self, "提示", "数据加载完毕，已解除", QMessageBox.Ok)
            self.data_file.close()
            if QMessageBox.Yes:
                self.name_label.setText("None")
                self.sex_label.setText("None")
                self.mode_label.setText("None")

                self.clear_all()
                self.simulateTimer.stop()
                self.procDataTimer.stop()
            else:
                return

    def JC_slot(self):
        QMessageBox.warning(self, "警告", "确定解除患者？", QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.Yes:
            self.name_label.setText("None")
            self.sex_label.setText("None")
            self.mode_label.setText("None")

            self.clear_all()

            self.CK_Dialog.open_slot()
        elif QMessageBox.No:
            return
    
    def clear_all(self):
        self.current_hr = 0
        self.current_resp = 0
        self.current_spo2 = 0
        self.current_pr = 0

        self.mPackAfterUnpackArr = []

        self.state_label.setText("正常")
        self.state_label.setStyleSheet("color: #00ff00")

        self.procDataTimer.stop()
        self.simulateTimer.stop()
        self.serialPortTimer.stop()
        self.updateTimer.stop()
 
        self.pixmapEcg.fill(Qt.black)
        self.pixmapSpo2.fill(Qt.black)
        self.pixmapResp.fill(Qt.black)

        self.ECG_wave.setPixmap(self.pixmapEcg)
        self.SPO2_wave.setPixmap(self.pixmapSpo2)
        self.RESP_wave.setPixmap(self.pixmapResp)

        self.mECG1WaveList = []
        self.mRESPWaveList = []
        self.mSPO2WaveList = []

        self.mEcgXStep = 0
        self.mRespXStep = 0
        self.mSpo2XStep = 0

        self.DL1_label.setStyleSheet("color: #ff0000")
        self.DL2_label.setStyleSheet("color: #ff0000")
        self.DL3_label.setStyleSheet("color: #000000")
        self.DL4_label.setStyleSheet("color: #000000")

        self.saveDataPath = ""
        self.is_alarming = False

        self.HR_label.setText("0")
        self.HR_label.setStyleSheet("color: #00ff00")
        self.RESP_label.setText("0")
        self.RESP_label.setStyleSheet("color: #ffb200")
        self.SpO2_label.setText("0")
        self.SpO2_label.setStyleSheet("color: #00ffee")
        self.PR_label.setText("0")
        self.PR_label.setStyleSheet("color: #00ffee")

    def update_time(self):
        """更新时间显示"""
        current_time = QDateTime.currentDateTime()
        string = current_time.toString("yyyy-MM-dd HH:mm:ss")
        data_str = string.split(" ")[0]
        time_str = string.split(" ")[1]

        self.date_label.setText(data_str)
        self.time_label.setText(time_str)

    def text_slot(self, set_signal):
        if set_signal == 1:
            self.name_label.setText(self.Info_Dialog.lineEdit.text())
            self.id_label.setText(self.Info_Dialog.id_lineEdit.text())
            self.sex_label.setText(self.Info_Dialog.comboBox.currentText())
            self.mode_label.setText(self.Info_Dialog.comboBox_2.currentText())

            if self.mode_label.text() == "成人":
                self.HR_threshold_low = 60
                self.HR_threshold_high = 100
                self.RESP_threshold_low = 12
                self.RESP_threshold_high = 24
                self.SPO2_threshold_low = 94
                self.PR_threshold_low = 60
                self.PR_threshold_high = 100

            elif "新生儿" in self.mode_label.text():
                self.HR_threshold_low = 100
                self.HR_threshold_high = 160
                self.RESP_threshold_low = 30
                self.RESP_threshold_high = 60
                self.SPO2_threshold_low = 92
                self.PR_threshold_low = 120
                self.PR_threshold_high = 160

            elif "婴儿" in self.mode_label.text():
                self.HR_threshold_low = 90
                self.HR_threshold_high = 150
                self.RESP_threshold_low = 30
                self.RESP_threshold_high = 50
                self.SPO2_threshold_low = 92
                self.PR_threshold_low = 80
                self.PR_threshold_high = 140

            elif "幼儿" in self.mode_label.text():
                self.HR_threshold_low = 70
                self.HR_threshold_high = 110
                self.RESP_threshold_low = 25
                self.RESP_threshold_high = 40
                self.SPO2_threshold_low = 94
                self.PR_threshold_low = 80
                self.PR_threshold_high = 130

            elif "学龄前" in self.mode_label.text():
                self.HR_threshold_low = 65
                self.HR_threshold_high = 110
                self.RESP_threshold_low = 20
                self.RESP_threshold_high = 34
                self.SPO2_threshold_low = 94
                self.PR_threshold_low = 75
                self.PR_threshold_high = 120

            elif "学龄" in self.mode_label.text():
                self.HR_threshold_low = 60
                self.HR_threshold_high = 95
                self.RESP_threshold_low = 18
                self.RESP_threshold_high = 30
                self.SPO2_threshold_low = 94
                self.PR_threshold_low = 60
                self.PR_threshold_high = 100

            elif "青少年" in self.mode_label.text():
                self.HR_threshold_low = 60
                self.HR_threshold_high = 100
                self.RESP_threshold_low = 12
                self.RESP_threshold_high = 20
                self.SPO2_threshold_low = 94
                self.PR_threshold_low = 60
                self.PR_threshold_high = 100            

            self.THRESHOLD_SIGNAL.emit(self.HR_threshold_low, self.HR_threshold_high, self.RESP_threshold_low, self.RESP_threshold_high, self.SPO2_threshold_low, self.PR_threshold_high, self.PR_threshold_low)

            self.Info_Dialog.close()
        elif set_signal == 0:
            QMessageBox.critical(self, "Error", "请填入姓名！")
            return
        
    def threshold_slot(self, hr_low, hr_high, resp_low, resp_high, spo2_low, pr_high, pr_low):
        self.HR_threshold_low = hr_low
        self.HR_threshold_high = hr_high
        self.RESP_threshold_low = resp_low
        self.RESP_threshold_high = resp_high
        self.SPO2_threshold_low = spo2_low
        self.PR_threshold_high = pr_high
        self.PR_threshold_low = pr_low
        QMessageBox.information(self, "提示", "阈值设置成功！")
        self.BJ_Dialog.close()

        self.THRESHOLD_SIGNAL.emit(self.HR_threshold_low, self.HR_threshold_high, self.RESP_threshold_low, self.RESP_threshold_high, self.SPO2_threshold_low, self.PR_threshold_high, self.PR_threshold_low)

if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())

