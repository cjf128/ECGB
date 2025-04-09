import datetime
import math
import random
import sys
import serial
from CK_Dialog import CK_Dialog
from Info_Dialog import Info_Dialog
from PackUnpack import PackUnpack

from PyQt5.QtCore import QTimer, Qt
from PyQt5.QtWidgets import QApplication, QMainWindow, QMessageBox, QGraphicsScene, QGraphicsView, QFrame
from PyQt5.QtGui import QPainter, QPen, QBrush, QColor, QIcon, QGuiApplication, QPainterPath



class ECGB_Window(QMainWindow, ECGB_Window):
    def __init__(self):
        super(ECGB_Window, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setWindowTitle('ECGB')
        self.config()

    def config(self):
        self.CK_btn.clicked.connect(self.CK_slot)
        self.XX_btn.clicked.connect(self.Info_slot)

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
        # self.hr_update_timer = QTimer(self)
        # self.hr_update_timer.timeout.connect(self.update_hr_display)
        # self.hr_update_timer.start(1000)

    def CK_slot(self):
        self.CK_Dialog = CK_Dialog()
        self.CK_Dialog.setWindowModality(Qt.ApplicationModal) 
        self.CK_Dialog.show()
        self.CK_Dialog.serialSignal.connect(self.serial_slot)
        self.CK_Dialog.exec_()
    
    def serial_slot(self, portNum, baudRate, dataBits, stopBits, parity):
        if self.ser.isOpen():
            self.serialPortTimer.stop()
            self.procDataTimer.stop()
            try:
                self.ser.close()
            except:
                pass
            self.status_label.setText("串口已关闭")
            self.status_label.setStylesheet("color: #ff0000")
        else:
            if portNum == "COM1":
                self.status_label.setText("模拟数据已启动")
                self.status_label.setStyleSheet("color: #ffffff")
                # 启动模拟数据定时器
                self.simulated_timer = QTimer(self)
                self.simulated_timer.timeout.connect(self.generate_simulated_data)
                self.simulated_timer.start(20)  # 50Hz采样率（20ms间隔）
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
                self.serialPortTimer.start(2)

    # 在类定义中添加以下方法
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
        
        # 使用协议类打包数据
        if self.mPackUnpck.packData(raw_packet):
            # 获取打包后的字节流
            packed_data = bytes(raw_packet)
            # 模拟接收数据处理
            self.process_received_data(packed_data)

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
    
    def data_receive(self):
        try:
            num = self.ser.inWaiting()
        except:
            self.serialPortTimer.stop()
            self.procDataTimer.stop()
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

    
    def Info_slot(self):
        self.Info_Dialog = Info_Dialog()
        self.Info_Dialog.setWindowModality(Qt.ApplicationModal)
        self.Info_Dialog.setSignal.connect(self.text_slot)
        self.Info_Dialog.show()
        self.Info_Dialog.exec_()
    
    def text_slot(self, set_signal):
        if set_signal == 1:
            self.name_label.setText(self.Info_Dialog.lineEdit.text())
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


if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = ECGB_Window()
    window.show()
    sys.exit(app.exec_())
