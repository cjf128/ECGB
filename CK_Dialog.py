import sys
from PyQt5.QtWidgets import QApplication, QDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtSerialPort import QSerialPortInfo
from PyQt5.QtGui import QIcon
from ui_CK_Dialog import Ui_CK_Dialog


class CK_Dialog(QDialog, Ui_CK_Dialog):
    serialSignal = pyqtSignal(str, str, str, str, str)

    def __init__(self, parent=None):
        super(CK_Dialog, self).__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
        self.setFixedSize(300, 300)
        
        self.config()
        self.serial_search()

    def config(self):
        self.Open_btn.clicked.connect(self.open_slot)
        self.Cancel_btn.clicked.connect(self.cancel_slot)
        self.btnUpdate.clicked.connect(self.serial_search)

    def serial_search(self):
        port_lsit = QSerialPortInfo.availablePorts()
        if len(port_lsit) >= 1:
            self.CKH_box.clear()
            for i in port_lsit:
                self.CKH_box.addItem(i.portName())

    def open_slot(self):
        self.serialSignal.emit(self.CKH_box.currentText(),
                            self.BTL_box.currentText(),
                            self.Data_box.currentText(),
                            self.Stop_box.currentText(),
                            self.JYW_box.currentText())
        self.close()

    def cancel_slot(self):
        self.close()
 


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CK_Dialog()
    window.show()
    sys.exit(app.exec_())