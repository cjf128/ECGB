import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtGui import QIcon

from ui_SJ_Dialog import Ui_SJ_Dialog



class SJ_Dialog(QDialog, Ui_SJ_Dialog):
    setSignal = pyqtSignal(bool, bool, bool, bool)
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
        hr = self.checkBox.isChecked()
        resp = self.checkBox_2.isChecked()
        spo2 = self.checkBox_3.isChecked()
        bpm = self.checkBox_4.isChecked()
        self.setSignal.emit(hr, resp, spo2, bpm)

        self.close()
    
    def cancel_slot(self):
        self.close()


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SJ_Dialog()
    window.show()
    sys.exit(app.exec_())