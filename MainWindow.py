import datetime
import math
import random
import sys
from PyQt5.QtWidgets import QMainWindow, QFrame, QGraphicsScene, QMessageBox, QApplication, QDialog, QPushButton
from PyQt5.QtCore import QTimer, Qt, QDateTime, pyqtSignal
from PyQt5.QtGui import QIcon, QPainterPath, QPen, QColor, QGuiApplication
from PyQt5.QtMultimedia import QSound

import serial
from CK_Dialog import CK_Dialog
from Info_Dialog import Info_Dialog
from PackUnpack import PackUnpack

from test import AlarmDialog
from ui_MainWindow import Ui_ECGB_Window


class MainWindow(QMainWindow, Ui_ECGB_Window):
    def __init__(self):
        super(MainWindow, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setWindowTitle('ECGB')

        # 初始化报警阈值（默认值）
        self.alarm_thresholds = {
            'urgent': 120, 
            'normal': 100
        }
        
        # 报警音效初始化
        self.alarm_sound = QSound("alarm.wav")  # 推荐使用网页5/7的警报声
        
        # 创建设置按钮
        self.setting_btn = QPushButton("⚙", self)
        self.setting_btn.clicked.connect(self.show_setting_dialog)
        
        # 监测定时器
        self.monitor_timer = QTimer()
        self.monitor_timer.timeout.connect(self.check_heart_rate)
        self.monitor_timer.start(1000)  # 每秒检测

        # 创建定时器
        self.clock_timer = QTimer(self)
        self.clock_timer.timeout.connect(self.update_time)
        self.clock_timer.start(1000)

        self.CK_Dialog = CK_Dialog()
        self.CK_Dialog.setWindowModality(Qt.ApplicationModal) 
        self.CK_Dialog.hide()
        self.CK_Dialog.serialSignal.connect(self.serial_slot)

        self.Info_Dialog = Info_Dialog()
        self.Info_Dialog.setWindowModality(Qt.ApplicationModal)
        self.Info_Dialog.setSignal.connect(self.text_slot)

        self.HR_threshold = 70  # 心率阈值
        self.RESP_threshold = 14
        self.SPO2_threshold = 94

        self.config()
    
    def show_setting_dialog(self):
        dialog = AlarmDialog(self)
        dialog.urgent_spin.setValue(self.alarm_thresholds['urgent'])
        dialog.normal_spin.setValue(self.alarm_thresholds['normal'])
        
        if dialog.exec_() == QDialog.Accepted:
            # 保存新阈值
            self.alarm_thresholds['urgent'] = dialog.urgent_spin.value()
            self.alarm_thresholds['normal'] = dialog.normal_spin.value()
            
    def check_heart_rate(self):
        current_hr = self.current_hr  # 解析当前值
        
        if current_hr >= self.alarm_thresholds['urgent']:
            self.trigger_alarm(level='urgent')
        elif current_hr >= self.alarm_thresholds['normal']:
            self.trigger_alarm(level='normal')
        else:
            self.stop_alarm()

    def trigger_alarm(self, level):
        # 视觉提示
        self.HR_label.setStyleSheet("color: red;" if level=='urgent' else "color: orange;")
        
        # 声音提示
        if not self.alarm_sound.isPlaying():
            self.alarm_sound.play()
            
    def stop_alarm(self):
        self.HR_label.setStyleSheet("color: white;")
        self.alarm_sound.stop()

    def config(self):
        self.CK_btn.clicked.connect(self.CK_slot)
        self.XX_btn.clicked.connect(self.Info_Dialog.show)
        self.JC_btn.clicked.connect(self.JC_slot)

        self.serialPortTimer = QTimer(self)
        self.serialPortTimer.timeout.connect(self.data_receive)

        self.ser = serial.Serial()
        self.mPackUnpck = PackUnpack()
        self.mECG1WaveList = []
        self.mECG1XStep = 0

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
        
        # 波形更新定时器（50ms刷新）
        self.waveform_timer = QTimer(self)
        self.waveform_timer.timeout.connect(self.update_waveform)
        self.waveform_timer.start(50)

        # 添加心率更新定时器（每秒更新一次）
        self.hr_update_timer = QTimer(self)
        self.hr_update_timer.timeout.connect(self.update_hr_display)
        self.hr_update_timer.start(1000)

        # 信号模拟
        self.simulated_timer = QTimer(self)
        self.simulated_timer.timeout.connect(self.generate_simulated_data)

        self.current_hr = 0  # 初始化心率值

    def CK_slot(self):
        self.CK_Dialog.show()

        # if self.name_label.text() != "None":
        #     self.CK_Dialog.show()
        # else:
        #     QMessageBox.critical(self, "Error", "请先填写信息！")
        #     return
    
    def serial_slot(self, portNum, baudRate, dataBits, stopBits, parity):
        if self.simulated_timer.isActive() and self.waveform_timer.isActive():
            self.simulated_timer.stop()
            self.waveform_timer.stop()

            self.HR_waveform_scene.clear()
            self.RESP_waveform_scene.clear()
            self.SPO2_waveform_scene.clear()

            self.status_label.setText("串口已关闭")
            self.status_label.setStyleSheet("color: #ff0000")
            self.CK_Dialog.hide()
        else:
            if self.ser.isOpen():
                self.serialPortTimer.stop()
                try:
                    self.ser.close()
                except:
                    pass
                self.status_label.setText("串口已关闭")
                self.status_label.setStyleSheet("color: #ff0000")
                self.CK_Dialog.hide()
            else:
                if portNum == "COM1":
                    self.status_label.setText("模拟数据已启动")
                    self.status_label.setStyleSheet("color: #ffffff")
                    # 启动模拟数据定时器
                    self.simulated_timer.start(20)  # 50Hz采样率（20ms间隔）
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
                    self.status_label.setText("串口已打开")
                    self.status_label.setStylesheet("color: #ffffff")
                    self.serialPortTimer.start(20)
                    self.CK_Dialog.Open_btn.setText("关闭串口")
                    self.CK_Dialog.hide()

    def generate_simulated_data(self):
        """生成符合协议规范的心电模拟数据"""
        # 创建原始数据包（模块ID + 数据头 + 二级ID + 6数据 + 校验和）
        module_id = 0x01        # 假设心电模块ID为0x01
        sub_id = 0xA1           # 二级ID（假设为心电波形）
        
        # 生成心电数值（示例用正弦波，范围0-4095）
        timestamp = datetime.datetime.now().timestamp()
        ecg_value = int(2048 * math.sin(2 * math.pi * 1.2 * timestamp) + 2048)
        
        # 构造原始数据包（注意长度必须为10）
        raw_packet = [
            module_id,   # 位置0: 模块ID
            0x00,        # 位置1: 数据头（将由packData填充）
            sub_id,      # 位置2: 二级ID
            (ecg_value >> 8) & 0xFF,  # 高位字节（位置3）
            ecg_value & 0xFF,         # 低位字节（位置4）
            0x00,        # 位置5: 保留字节
            0x00,        # 位置6: 保留字节
            0x00,        # 位置7: 保留字节
            0x00,        # 位置8: 保留字节
            0x00         # 位置9: 校验和（将由packData填充）
        ]

        # 模拟心率波动（±5BPM随机变化）
        base_hr = 72  # 基础心率值
        hr_variation = random.randint(-5, 5)
        self.current_hr = base_hr + hr_variation
        
        # 使用协议类打包数据
        if self.mPackUnpck.packData(raw_packet):
            # 获取打包后的字节流
            packed_data = bytes(raw_packet)
            # 模拟接收数据处理
            self.process_received_data(packed_data)

    def update_hr_display(self):
        """更新心率显示标签"""
        self.HR_label.setText(f"{self.current_hr}")
        if self.current_hr >= self.HR_threshold:
            self.HR_label.setStyleSheet("color: #ff0000")
        else:
            self.HR_label.setStyleSheet("color: #00ff00")
        
    def process_received_data(self, data):
        """处理接收到的二进制数据"""
        # 协议解析（逐个字节处理）
        for byte in data:
            if self.mPackUnpck.unpackData(byte):
                # 成功解析到完整包时获取数据
                unpacked = self.mPackUnpck.getUnpackRslt()
                # 提取有效数值（根据协议结构）
                ecg_value = (unpacked[3] << 8) | unpacked[4]
                # 转换为有符号数（示例协议使用无符号，根据实际调整）
                self.mECG1WaveList.append(ecg_value - 2048)  # 转换为±2048范围
                
                # 保持数据队列长度
                max_points = 5 * 250  # 存储5秒数据（假设250Hz采样率）
                self.mECG1WaveList = self.mECG1WaveList[-max_points:]

                # 根据协议结构获取心率值（示例：假设心率在位置5-6）
                # if unpacked[0] == 0x01:  # 确认模块ID
                #     if unpacked[2] == 0xB1:  # 确认二级ID为心率
                #         # 解析16位心率值（大端序）
                #         self.current_hr = (unpacked[5] << 8) | unpacked[6]
            
    
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.serialPortTimer.stop()
            try:
                self.ser.close()
            except:
                pass
            return None
        if num > 0:
            data = self.ser.read(num)
            strUnPack = ""
            if self.showHexCheckBox.isChecked():
                out_s = ''
                for i in range(0, len(data)):
                    out_s = out_s + '{:02X}'.format(data[i]) + ' '
        else:
            pass

     # 处理已解包的数据   
    def data_process(self):
        num = len(self.mPackAfterUnpackArr)  # 列表数据长度
        if num > 0:
            for i in range(num):
                if self.mPackAfterUnpackArr[i][0] == 0x10:  # 0x10:心电相关的数据包
                    self.analyzeECGData(self.mPackAfterUnpackArr[i])
            # 删掉已处理数据
            del self.mPackAfterUnpackArr[0:num]
        # 心电波形数据点大于10才开始画心电波形
        if len(self.mECG1WaveList) > 10:
            self.drawECG1Wave()
    
    def text_slot(self, set_signal):
        if set_signal == 1:
            self.name_label.setText(self.Info_Dialog.lineEdit.text())
            self.id_label.setText(self.Info_Dialog.id_lineEdit.text())
            self.sex_label.setText(self.Info_Dialog.comboBox.currentText())
            self.mode_label.setText(self.Info_Dialog.comboBox_2.currentText())
            self.Info_Dialog.close()
        elif set_signal == 0:
            QMessageBox.critical(self, "Error", "请填入姓名！")
            return
    
    def update_waveform(self):
        if not self.mECG1WaveList:
            return
        
        # 清空旧波形
        self.HR_waveform_scene.clear()
        self.RESP_waveform_scene.clear()
        self.SPO2_waveform_scene.clear()
        
        # 创建新路径
        path = QPainterPath()
        view_width = self.ecg1_graphicsView.width()
        view_height = self.ecg1_graphicsView.height()
        
        # 计算坐标参数
        x_step = 3  # 每个数据点间隔3像素
        max_points = view_width // x_step
        start_idx = max(0, len(self.mECG1WaveList) - max_points)
        y_scale = view_height / 4096  # 数据范围±2048
        y_offset = view_height / 2
        
        # 绘制路径
        x = 0
        path.moveTo(x, y_offset - self.mECG1WaveList[start_idx] * y_scale)
        for i in range(start_idx + 1, len(self.mECG1WaveList)):
            x += x_step
            y = y_offset - self.mECG1WaveList[i] * y_scale
            path.lineTo(x, y)
        
        # 绘制到场景
        self.HR_waveform_scene.addPath(path, QPen(QColor(0, 255, 0), 2))
        self.RESP_waveform_scene.addPath(path, QPen(QColor("#ffc300"), 2))
        self.SPO2_waveform_scene.addPath(path, QPen(QColor("#33e8dc"), 2))
        
        # 自动滚动视图
        if x > view_width * 0.8:
            self.ecg1_graphicsView.centerOn(x, y_offset)

    def JC_slot(self):
        QMessageBox.warning(self, "警告", "确定解除患者？", QMessageBox.Yes | QMessageBox.No)
        if QMessageBox.Yes:
            self.name_label.setText("None")
            self.sex_label.setText("None")
            self.mode_label.setText("None")
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



if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())
