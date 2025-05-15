
import copy
import datetime
import math
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QFrame, QGraphicsScene, QMessageBox, QApplication, QGraphicsPathItem
from PyQt5.QtCore import QTimer, Qt, QDateTime, pyqtSignal, QUrl
from PyQt5.QtGui import QIcon, QPainterPath, QPen, QGuiApplication, QFont, QColor
from PyQt5.QtMultimedia import QMediaPlayer, QMediaContent

import serial
from CK_Dialog import CK_Dialog
from Info_Dialog import Info_Dialog
from BJ_Dialog import BJ_Dialog
from PackUnpack import PackUnpack

from SJ_Dialog import SJ_Dialog
from ui_MainWindow import Ui_ECGB_Window


class MainWindow(QMainWindow, Ui_ECGB_Window):
    THRESHOLD_SIGNAL = pyqtSignal(int, int, int, int, int)
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
        self.setWindowTitle('ECGB')

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

        self.SJ_Dialog = SJ_Dialog()
        self.SJ_Dialog.setWindowTitle('数据保存')
        self.SJ_Dialog.setWindowModality(Qt.ApplicationModal)
        self.SJ_Dialog.setSignal.connect(self.SJ_slot)
        self.config()

    def config(self):
        self.CK_btn.clicked.connect(self.CK_slot)
        self.XX_btn.clicked.connect(self.Info_Dialog.show)
        self.JC_btn.clicked.connect(self.JC_slot)
        self.BJ_btn.clicked.connect(self.BJ_Dialog.show)
        self.SJ_btn.clicked.connect(self.SJ_Dialog.show)

        self.THRESHOLD_SIGNAL.connect(self.BJ_Dialog.threshold_slot)

        self.ser = serial.Serial()
        self.mPackUnpck = PackUnpack()
        self.mECG1WaveList = []
        self.mRESPWaveList = []
        self.mSPO2WaveList = []
        self.mBPMWaveList = []
        self.time_list = []

        self.HR_waveform_scene = QGraphicsScene()
        self.ecg1_graphicsView.setScene(self.HR_waveform_scene)
        self.ecg1_graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ecg1_graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.ecg1_graphicsView.setFrameShape(QFrame.NoFrame)
        
        self.RESP_waveform_scene = QGraphicsScene()
        self.resp2_graphicsView.setScene(self.RESP_waveform_scene)
        self.resp2_graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resp2_graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.resp2_graphicsView.setFrameShape(QFrame.NoFrame)

        self.SPO2_waveform_scene = QGraphicsScene()
        self.spo2_graphicsView.setScene(self.SPO2_waveform_scene)
        self.spo2_graphicsView.setHorizontalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.spo2_graphicsView.setVerticalScrollBarPolicy(Qt.ScrollBarAlwaysOff)
        self.spo2_graphicsView.setFrameShape(QFrame.NoFrame)

        # 时间更新定时器
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        # 添加心率更新定时器（每秒更新一次）
        self.hr_update_timer = QTimer(self)
        self.hr_update_timer.timeout.connect(self.update_hr_display)
        self.hr_update_timer.start(1000)

        # 添加呼吸率更新定时器（每秒更新一次）
        self.resp_update_timer = QTimer(self)
        self.resp_update_timer.timeout.connect(self.update_resp_display)
        self.resp_update_timer.start(1000)

        # 添加脉率更新定时器（每秒更新一次）
        self.spo2_update_timer = QTimer(self)
        self.spo2_update_timer.timeout.connect(self.update_spo2_display)
        self.spo2_update_timer.start(1000)

        # 信号模拟
        self.simulated_timer = QTimer(self)
        # self.simulated_timer.timeout.connect()

        self.serialPortTimer = QTimer(self)
        self.serialPortTimer.timeout.connect(self.data_receive)

        self.procDataTimer = QTimer(self)
        self.procDataTimer.timeout.connect(self.data_process)

        self.alarm_player = QMediaPlayer()
        self.alarm_player.setMedia(QMediaContent(QUrl.fromLocalFile('alarm.mp3')))
        self.is_alarming = False

        self.HR_threshold_low = 60
        self.HR_threshold_high = 100
        self.RESP_threshold_low = 12
        self.RESP_threshold_high = 24
        self.SPO2_threshold_low = 94
        self.maxPoints = 50

        self.simulated_state = False

        self.current_hr = 0
        self.current_resp = 0
        self.current_spo2 = 0

        self.HR_blink_state = False
        self.RESP_blink_state = False
        self.SPO2_blink_state = False
        self.BPM_blink_state = False

        self.mPackAfterUnpackArr = []
        self.saveDataPath = ""
        self.limit = 0


    def CK_slot(self):
        self.CK_Dialog.show()

        # if self.name_label.text() != "None":
        #     self.CK_Dialog.show()
        # else:
        #     QMessageBox.critical(self, "Error", "请先填写信息！")
        #     return
    
    def serial_slot(self, portNum, baudRate, dataBits, stopBits, parity):
        if self.simulated_state == True:
            self.simulated_timer.stop()

            self.HR_waveform_scene.clear()
            self.RESP_waveform_scene.clear()
            self.SPO2_waveform_scene.clear()

            self.status_label.setText("串口已关闭")
            self.status_label.setStyleSheet("color: #ff0000")
            self.CK_Dialog.Open_btn.setText("打开串口")
            self.CK_Dialog.hide()
            self.simulated_state = False
            return
        
        if self.ser.isOpen():
            self.serialPortTimer.stop()
            self.procDataTimer.stop()
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
        self.procDataTimer.start(2)

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
                    if self.limit < 446:
                        with open(self.saveDataPath, 'a') as file:
                            data = []
                            for j in range(0, 8):
                                data.append(self.mPackAfterUnpackArr[i][j])
                            file.write(str(data) + '\n')
                            self.limit += 1
                    else:
                        self.saveDataPath = ''
                        self.limit = 0
            del self.mPackAfterUnpackArr[0:num]

        if len(self.mECG1WaveList) > 10:
            self.drawECGWave()
        if len(self.mRESPWaveList) > 10:
            self.drawRESPWave()
        if len(self.mSPO2WaveList) > 10:
            self.drawSPO2Wave()

    def analyzeECGData(self, data):
        if data[1] == 0x02:
            ecgData1 = data[2] << 8 | data[3]
            ecgData2 = data[4] << 8 | data[5]
            if ecgData1 != 0:
                self.mECG1WaveList.append(ecgData1)
            if ecgData2 != 0:
                self.mECG1WaveList.append(ecgData2)
        elif data[1] == 0x03:
            if data[2] == 1:
                self.DL1_label.setStyleSheet("color:red")
            else:
                self.DL1_label.setStyleSheet("color:green")
        elif data[1] == 0x04:
            self.current_hr = data[2] << 8 | data[3]
            if self.current_hr != 0:
                self.HR_label.setText(str(self.current_hr))

    def analyzeRESPData(self, data):
        if data[1] == 0x02:
            resp = data[2] << 8 | data[3]
            self.mRESPWaveList.append(resp)
        elif data[1] == 0x03:
            self.current_resp = data[2] << 8 | data[3]
            self.RESP_label.setText(str(self.current_resp))
        elif data[1] == 0x06:
            if data[2] == 1:
                self.DL2_label.setStyleSheet("color:green")
            else:
                self.DL2_label.setStyleSheet("color:red")

    # 处理血氧数据
    def analyzeSPO2Data(self, data):
        if data[1] == 0x02:
            spo2Data = data[2] << 8 | data[3]
            if spo2Data != 0:
                self.mSPO2WaveList.append(spo2Data)
        elif data[1] == 0x04:
            if data[2] == 0x01:
                self.DL3_label.setText("手指脱落")
                self.DL3_label.setStyleSheet("color:red")
        elif data[1] == 0x05:
            if data[2] == 0x01:
                self.DL4_label.setText("探头脱落")
                self.DL4_label.setStyleSheet("color:red")
        elif data[1] == 0x03:
            self.current_spo2 = data[3]
            self.SpO2_label.setText(str(self.current_spo2))

    def drawECGWave(self):
        if not self.mECG1WaveList:
            return

        # 清除旧内容（可选）
        self.HR_waveform_scene.clear()

        view_width = self.ecg1_graphicsView.width()
        view_height = self.ecg1_graphicsView.height()

        scale_x = view_width / self.maxPoints
        scale_y = view_height / 2 / 4096

        path = QPainterPath()
        path.moveTo(0, (self.mECG1WaveList[0] - 2048) * scale_y + view_height / 2)

        for i in range(1, len(self.mECG1WaveList)):
            x = i * scale_x
            y = (self.mECG1WaveList[i] - 2048) * scale_y + view_height / 2
            path.lineTo(x, y)

        path_item = QGraphicsPathItem(path)
        path_item.setPen(QPen(QColor("#25e81e"), 2))
        self.HR_waveform_scene.addItem(path_item)

        # 保留最近 maxPoints 个点
        if len(self.mECG1WaveList) > self.maxPoints:
            self.mECG1WaveList = self.mECG1WaveList[-self.maxPoints:]

        if not self.mECG1WaveList:
            return
    
    def drawRESPWave(self):
        if not self.mRESPWaveList:
            return

        # 清除旧内容（可选）
        self.RESP_waveform_scene.clear()

        view_width = self.resp2_graphicsView.width()
        view_height = self.resp2_graphicsView.height()

        scale_x = view_width / self.maxPoints
        scale_y = view_height / 2 / 4096

        path = QPainterPath()
        path.moveTo(0, (self.mRESPWaveList[0] - 2048) * scale_y + view_height / 2)

        for i in range(1, len(self.mRESPWaveList)):
            x = i * scale_x
            y = (self.mRESPWaveList[i] - 2048) * scale_y + view_height / 2
            path.lineTo(x, y)

        path_item = QGraphicsPathItem(path)
        path_item.setPen(QPen(QColor("#ffc300"), 2))
        self.RESP_waveform_scene.addItem(path_item)

        # 保留最近 maxPoints 个点
        if len(self.mRESPWaveList) > self.maxPoints:
            self.mRESPWaveList = self.mRESPWaveList[-self.maxPoints:]

        if not self.mRESPWaveList:
            return
    
    def drawSPO2Wave(self):
        if not self.mSPO2WaveList:
            return

        # 清除旧内容（可选）
        self.SPO2_waveform_scene.clear()

        view_width = self.spo2_graphicsView.width()
        view_height = self.spo2_graphicsView.height()

        scale_x = view_width / self.maxPoints
        scale_y = view_height / 2 / 4096

        path = QPainterPath()
        path.moveTo(0, (self.mSPO2WaveList[0] - 2048) * scale_y + view_height / 2)

        for i in range(1, len(self.mSPO2WaveList)):
            x = i * scale_x
            y = (self.mSPO2WaveList[i] - 2048) * scale_y + view_height / 2
            path.lineTo(x, y)

        path_item = QGraphicsPathItem(path)
        path_item.setPen(QPen(QColor("#33e8dc"), 2))
        self.SPO2_waveform_scene.addItem(path_item)

        # 保留最近 maxPoints 个点
        if len(self.mSPO2WaveList) > self.maxPoints:
            self.mSPO2WaveList = self.mSPO2WaveList[-self.maxPoints:]

        if not self.mSPO2WaveList:
            return

    def update_hr_display(self):
        """更新心率显示标签"""
        self.HR_label.setText(f"{self.current_hr}")
        if self.current_hr >= self.HR_threshold_high or self.current_hr > 0 and self.current_hr <= self.HR_threshold_low:
            if not self.is_alarming:
                self.alarm_player.play()
                self.is_alarming = True

            if self.alarm_player.state() != QMediaPlayer.PlayingState:
                self.alarm_player.play()
                    
            if self.hr_update_timer.interval() != 500:
                self.hr_update_timer.setInterval(500) # 周期改为500ms
                self.hr_update_timer.start()

            if self.HR_blink_state:
                self.HR_label.setFont(QFont("Agency FB", 120))
                self.HR_label.setStyleSheet("color: #ff0000")
            else:
                self.HR_label.setFont(QFont("Agency FB", 130))
                self.HR_label.setStyleSheet("color: #FFFFFF")

            self.HR_blink_state = not self.HR_blink_state
        else:
            if self.is_alarming:
                self.alarm_player.stop()
                self.is_alarming = False

            if self.hr_update_timer.interval() != 1000:
                self.hr_update_timer.setInterval(1000)
                self.hr_update_timer.start()
            self.HR_label.setFont(QFont("Agency FB", 120))
            self.HR_label.setStyleSheet("color: #00ff00")  # 绿色
            self.HR_blink_state = False  # 重置闪烁状态

    def update_resp_display(self):
        """更新呼吸率显示标签"""
        self.RESP_label.setText(f"{self.current_resp}")
        if self.current_resp >= self.RESP_threshold_high or self.current_resp > 0 and self.current_resp <= self.RESP_threshold_low:
            if not self.is_alarming:
                self.alarm_player.play()
                self.is_alarming = True

            if self.alarm_player.state() != QMediaPlayer.PlayingState:
                self.alarm_player.play()
                    
            if self.resp_update_timer.interval() != 500:
                self.resp_update_timer.setInterval(500) # 周期改为500ms
                self.resp_update_timer.start()

            if self.RESP_blink_state:
                self.RESP_label.setFont(QFont("Agency FB", 120))
                self.RESP_label.setStyleSheet("color: #ff0000")
            else:
                self.RESP_label.setFont(QFont("Agency FB", 130))

            self.RESP_blink_state = not self.RESP_blink_state
        else:
            if self.is_alarming:
                self.alarm_player.stop()
                self.is_alarming = False

            if self.resp_update_timer.interval() != 1000:
                self.resp_update_timer.setInterval(1000)
                self.resp_update_timer.start()
            self.RESP_label.setFont(QFont("Agency FB", 120))
            self.RESP_label.setStyleSheet("color: #ffc300")
            self.RESP_blink_state = False  # 重置闪烁状态

    def update_spo2_display(self):
        """更新脉率显示标签"""
        self.SpO2_label.setText(f"{self.current_spo2}")
        self.BPM_label.setText(f"{self.current_hr}")
        if self.current_spo2 > 0 and self.current_spo2 <= self.SPO2_threshold_low:
            if not self.is_alarming:
                self.alarm_player.play()
                self.is_alarming = True

            if self.alarm_player.state() != QMediaPlayer.PlayingState:
                self.alarm_player.play()
                    
            if self.spo2_update_timer.interval() != 500:
                self.spo2_update_timer.setInterval(500)
                self.spo2_update_timer.start()

            if self.SPO2_blink_state:
                self.SpO2_label.setFont(QFont("Agency FB", 80))
                self.SpO2_label.setStyleSheet("color: #ff0000")
            else:
                self.SpO2_label.setFont(QFont("Agency FB", 90))

            self.SPO2_blink_state = not self.SPO2_blink_state

            if self.BPM_blink_state:
                self.BPM_label.setFont(QFont("Agency FB", 80))
                self.BPM_label.setStyleSheet("color: #ff0000")
            else:
                self.BPM_label.setFont(QFont("Agency FB", 90))

            self.BPM_blink_state = not self.BPM_blink_state

        else:
            if self.is_alarming:
                self.alarm_player.stop()
                self.is_alarming = False

            if self.spo2_update_timer.interval() != 1000:
                self.spo2_update_timer.setInterval(1000)
                self.spo2_update_timer.start()
            self.SpO2_label.setFont(QFont("Agency FB", 80))
            self.SpO2_label.setStyleSheet("color: #33e8dc")

            self.BPM_label.setFont(QFont("Agency FB", 80))
            self.BPM_label.setStyleSheet("color: #33e8dc")
            self.SPO2_blink_state = False
            self.BPM_blink_state = False

    def SJ_slot(self, path):
        self.saveDataPath = path
        


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

        self.hr_update_timer.stop()
        self.resp_update_timer.stop()
        self.spo2_update_timer.stop()

        self.HR_waveform_scene.clear()
        self.RESP_waveform_scene.clear()
        self.SpO2_waveform_scene.clear()

        self.mECG1WaveList = []
        self.mBPMWaveList = []
        self.mSPO2WaveList = []

        self.HR_label.setText("0")
        self.RESP_label.setText("0")
        self.SpO2_label.setText("0")
        self.BPM_label.setText("0")
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

            elif "新生儿" in self.mode_label.text():
                self.HR_threshold_low = 100
                self.HR_threshold_high = 160
                self.RESP_threshold_low = 30
                self.RESP_threshold_high = 60
                self.SPO2_threshold_low = 92

            elif "婴儿" in self.mode_label.text():
                self.HR_threshold_low = 90
                self.HR_threshold_high = 150
                self.RESP_threshold_low = 30
                self.RESP_threshold_high = 50
                self.SPO2_threshold_low = 92

            elif "幼儿" in self.mode_label.text():
                self.HR_threshold_low = 70
                self.HR_threshold_high = 110
                self.RESP_threshold_low = 25
                self.RESP_threshold_high = 40
                self.SPO2_threshold_low = 94

            elif "学龄前" in self.mode_label.text():
                self.HR_threshold_low = 65
                self.HR_threshold_high = 110
                self.RESP_threshold_low = 20
                self.RESP_threshold_high = 34
                self.SPO2_threshold_low = 94

            elif "学龄" in self.mode_label.text():
                self.HR_threshold_low = 60
                self.HR_threshold_high = 95
                self.RESP_threshold_low = 18
                self.RESP_threshold_high = 30
                self.SPO2_threshold_low = 94

            elif "青少年" in self.mode_label.text():
                self.HR_threshold_low = 60
                self.HR_threshold_high = 100
                self.RESP_threshold_low = 12
                self.RESP_threshold_high = 20
                self.SPO2_threshold_low = 94

            self.THRESHOLD_SIGNAL.emit(self.HR_threshold_low, self.HR_threshold_high, self.RESP_threshold_low, self.RESP_threshold_high, self.SPO2_threshold_low)

            self.Info_Dialog.close()
        elif set_signal == 0:
            QMessageBox.critical(self, "Error", "请填入姓名！")
            return
        
    def threshold_slot(self, hr_low, hr_high, resp_low, resp_high, spo2_low):
        self.HR_threshold_low = hr_low
        self.HR_threshold_high = hr_high
        self.RESP_threshold_low = resp_low
        self.RESP_threshold_high = resp_high
        self.SPO2_threshold_low = spo2_low
        QMessageBox.information(self, "提示", "阈值设置成功！")

        self.THRESHOLD_SIGNAL.emit(self.HR_threshold_low, self.HR_threshold_high, self.RESP_threshold_low, self.RESP_threshold_high, self.SPO2_threshold_low)

        self.BJ_Dialog.close()
    


if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
