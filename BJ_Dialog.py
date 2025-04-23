import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtGui import QIcon

from ui_BJ_Dialog import Ui_BJ_Dialog


class BJ_Dialog(QDialog, Ui_BJ_Dialog):
    thresholdSignal = pyqtSignal(int, int, int, int, int)

    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setFixedSize(self.sizeHint())
        self.config()
    
    def config(self):
        self.pushButton.clicked.connect(self.set_slot)
        self.pushButton_2.clicked.connect(self.cancel_slot)
 
    def set_slot(self):
        self.thresholdSignal.emit(self.spinBox.value(), self.spinBox_2.value(), self.spinBox_3.value(), self.spinBox_4.value(), self.spinBox_5.text())
        self.close()
    
    def cancel_slot(self):
        self.close()

    def threshold_slot(self, hr_low, hr_high, resp_low, resp_high, spo2_low):
        self.spinBox.setValue(hr_low)
        self.spinBox_2.setValue(hr_high)
        self.spinBox_3.setValue(resp_low)
        self.spinBox_4.setValue(resp_high)
        self.spinBox_5.setValue(spo2_low)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = BJ_Dialog()
    window.show()
    sys.exit(app.exec_())