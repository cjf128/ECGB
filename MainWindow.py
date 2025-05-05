
import copy
import math
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QFrame, QGraphicsScene, QMessageBox, QApplication, QDialog, QPushButton
from PyQt5.QtCore import QTimer, Qt, QDateTime, pyqtSignal, QUrl
from PyQt5.QtGui import QIcon, QPainterPath, QPen, QColor, QGuiApplication, QFont
from PyQt5.QtMultimedia import QSound, QMediaPlayer, QMediaContent

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
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
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
        self.SJ_btn.clicked.connect(self.SJ_slot)

        self.THRESHOLD_SIGNAL.connect(self.BJ_Dialog.threshold_slot)

        self.serialPortTimer = QTimer(self)
        self.serialPortTimer.timeout.connect(self.data_receive)

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
        
        # 波形更新定时器
        self.waveform_hr_timer = QTimer(self)
        self.waveform_hr_timer.timeout.connect(self.update_hr_waveform)

        self.waveform_resp_timer = QTimer(self)
        self.waveform_resp_timer.timeout.connect(self.update_resp_waveform)

        self.waveform_spo2_timer = QTimer(self)
        self.waveform_spo2_timer.timeout.connect(self.update_spo2_waveform)

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
        self.simulated_timer.timeout.connect(self.generate_simulated_data)

        self.alarm_player = QMediaPlayer()
        self.alarm_player.setMedia(QMediaContent(QUrl.fromLocalFile('alarm.mp3')))
        self.is_alarming = False

        self.HR_threshold_low = 60
        self.HR_threshold_high = 100
        self.RESP_threshold_low = 12
        self.RESP_threshold_high = 24
        self.SPO2_threshold_low = 94

        self.simulated_time = 1
        self.simulated_state = False

        self.current_hr = 0
        self.current_resp = 0
        self.current_spo2 = 0

        self.HR_blink_state = False
        self.RESP_blink_state = False
        self.SPO2_blink_state = False
        self.BPM_blink_state = False


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
            self.waveform_hr_timer.stop()
            self.waveform_resp_timer.stop()
            self.waveform_spo2_timer.stop()

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
            try:
                self.ser.close()
            except:
                pass
            self.status_label.setText("串口已关闭")
            self.status_label.setStyleSheet("color: #ff0000")
            self.CK_Dialog.Open_btn.setText("打开串口")
            self.CK_Dialog.hide()
            return
        

        if portNum == "COM1":
            self.simulated_state = True
            self.status_label.setText("模拟数据已启动")
            self.status_label.setStyleSheet("color: #ffffff")

            # 启动模拟数据定时器
            self.waveform_hr_timer.start(20)
            self.waveform_resp_timer.start(20)
            self.waveform_spo2_timer.start(20)

            self.simulated_timer.start(20)
            self.CK_Dialog.Open_btn.setText("关闭串口")
            self.CK_Dialog.hide() # 串口对话框
        else:
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

            self.serialPortTimer.start(20)
            self.waveform_hr_timer.start(20)
            self.waveform_resp_timer.start(20)
            self.waveform_spo2_timer.start(20)

            self.status_label.setText("串口已打开")
            self.status_label.setStyleSheet("color: #ffffff")
            self.CK_Dialog.Open_btn.setText("关闭串口")
            self.CK_Dialog.hide()
    
    def data_receive(self):
        """实时接收串口数据"""
        if self.ser.isOpen():
            try:
                # 获取接收缓冲区字节数
                bytes_to_read = self.ser.in_waiting
                if bytes_to_read > 0:
                    # 读取所有可用数据
                    received_data = self.ser.read(bytes_to_read)
                    # 调用协议解析方法
                    self.process_received_data(received_data)
            except Exception as e:
                self.status_label.setText(f"接收错误: {str(e)}")
                self.status_label.setStyleSheet("color: #ff0000")
    
    def process_received_data(self, data):
        """处理接收到的二进制数据"""
        # 协议解析（逐个字节处理）
        for byte in data:
            if self.mPackUnpck.unpackData(byte):
                # 成功解析到完整包时获取数据
                unpacked = self.mPackUnpck.getUnpackRslt()

                if unpacked[0] == 0x13:  # 确认模块ID
                    if unpacked[2] == 0x02:  # 确认二级ID为心率
                        # 解析血氧
                        self.current_spo2 = (unpacked[3] << 8) | unpacked[4]
                        self.mSPO2WaveList.append(self.current_spo2)

                        # 保持数据队列长度
                        max_points = 10 * 50
                        self.mSPO2WaveList = self.mSPO2WaveList[-max_points:]
            
    def generate_simulated_data(self):
        """生成符合协议规范的心电模拟数据"""
        # 生成心电数值
        ecg_value = int(0.1 * math.sin(2 * math.pi * self.simulated_time) + 72 + random.uniform(-6, 6))
        resp_value = int(0.1 * math.sin(2 * math.pi * self.simulated_time) + 18 + random.uniform(-6, 6))
        spo2_value = int(0.1 * math.sin(2 * math.pi * self.simulated_time) + 97 + random.uniform(-3, 3))

        # 创建原始数据包（模块ID + 数据头 + 二级ID + 6数据 + 校验和）
        module_id = 0x01        # 假设心电模块ID为0x01
        if self.simulated_time % 3 == 0:
            sub_id = 0xA1           # 二级ID（假设为心电波形）
            value = ecg_value
        elif self.simulated_time % 3 == 1:
            sub_id = 0xB1
            value = resp_value
        elif self.simulated_time % 3 == 2:
            sub_id = 0xC1
            value = spo2_value

        self.simulated_time += 1
        
        # 构造原始数据包（注意长度必须为10）
        raw_packet = [
            module_id,   # 位置0: 模块ID
            0x00,        # 位置1: 数据头（将由packData填充）
            sub_id,      # 位置2: 二级ID
            (value >> 8) & 0xFF,  # 高位字节（位置3）
            value & 0xFF,         # 低位字节（位置4）
            0x00,        # 位置5: 保留字节
            0x00,        # 位置6: 保留字节
            0x00,        # 位置7: 保留字节
            0x00,        # 位置8: 保留字节
            0x00         # 位置9: 校验和（将由packData填充）
        ]

        # 使用协议类打包数据
        if self.mPackUnpck.packData(raw_packet):
            # 获取打包后的字节流
            packed_data = bytes(raw_packet)
            # 模拟接收数据处理
            self.process_received_data(packed_data)

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
        
    
    def update_hr_waveform(self):
        if not self.mECG1WaveList:
            return
        
        # 清空旧波形
        self.HR_waveform_scene.clear()
        
        # 创建新路径
        path = QPainterPath()
        view_width = self.ecg1_graphicsView.width()
        view_height = self.ecg1_graphicsView.height()
        
        # 计算坐标参数
        x_step = 3
        max_points = view_width // x_step
        start_idx = max(0, len(self.mECG1WaveList) - max_points)
        y_scale = 6
        y_offset = view_height / 50
        
        # 绘制路径
        x = 0
        path.moveTo(x, y_offset - self.mECG1WaveList[start_idx] * y_scale)
        for i in range(start_idx + 1, len(self.mECG1WaveList)):
            x += x_step
            y = y_offset - self.mECG1WaveList[i] * y_scale
            path.lineTo(x, y)
        
        # 绘制到场景
        self.HR_waveform_scene.addPath(path, QPen(QColor("#00ff00"), 2))
        
        # 自动滚动视图
        if x > view_width * 0.8:
            self.ecg1_graphicsView.centerOn(x, y_offset)

    def update_resp_waveform(self):
        if not self.mRESPWaveList:
            return
        
        # 清空旧波形
        self.RESP_waveform_scene.clear()
        
        # 创建新路径
        path = QPainterPath()
        view_width = self.resp2_graphicsView.width()
        view_height = self.resp2_graphicsView.height()
        
        # 计算坐标参数
        x_step = 3
        max_points = view_width// x_step
        start_idx = max(0, len(self.mRESPWaveList) - max_points)
        y_scale = 6
        y_offset = view_height / 50

        # 绘制路径
        x = 0
        path.moveTo(x, y_offset - self.mRESPWaveList[start_idx] * y_scale)
        for i in range(start_idx + 1, len(self.mRESPWaveList)):
            x += x_step
            y = y_offset - self.mRESPWaveList[i] * y_scale
            path.lineTo(x, y)
        
        # 绘制到场景
        self.RESP_waveform_scene.addPath(path, QPen(QColor("#ffc300"), 2))
        # 自动滚动视图
        if x > view_width * 0.8:
            self.resp2_graphicsView.centerOn(x, y_offset)

    def update_spo2_waveform(self):
        if not self.mSPO2WaveList:
            return
        
        # 清空旧波形
        self.SPO2_waveform_scene.clear()

        # 创建新路径
        path = QPainterPath()
        view_width = self.spo2_graphicsView.width()
        view_height = self.spo2_graphicsView.height()
        
        # 计算坐标参数
        x_step = 3
        max_points = view_width // x_step
        start_idx = max(0, len(self.mSPO2WaveList) - max_points)
        y_scale = 6
        y_offset = view_height / 50

        # 绘制路径
        x = 0
        path.moveTo(x, y_offset - self.mSPO2WaveList[start_idx] * y_scale)
        for i in range(start_idx + 1, len(self.mSPO2WaveList)):
            x += x_step
            y = y_offset - self.mSPO2WaveList[i] * y_scale
            path.lineTo(x, y)
        
        # 绘制到场景
        self.SPO2_waveform_scene.addPath(path, QPen(QColor("#33e8dc"), 2))

        # 自动滚动视图
        if x > view_width * 0.8:
            self.spo2_graphicsView.centerOn(x, y_offset)


    def JC_slot(self):
        QMessageBox.warning(self, "警告", "确定解除患者？", QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.Yes and self.simulated_state:
            self.name_label.setText("None")
            self.sex_label.setText("None")
            self.mode_label.setText("None")

            self.current_hr = 0

            self.CK_Dialog.open_slot()
        elif QMessageBox.No:
            return
    
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
    
    def SJ_slot(self, hr, resp, spo2, bpm):
        pass


if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
