import sys
from PyQt5.QtWidgets import QDialog, QApplication
from PyQt5.QtGui import QIcon
from PyQt5.QtCore import pyqtSignal

from ui_Info_Dialog import Ui_Info_Dialog

class Info_Dialog(QDialog, Ui_Info_Dialog):
    setSignal = pyqtSignal(bool)

    def __init__(self, parent=None):
        super(Info_Dialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setFixedSize(250, 250)
        self.config()

    def config(self):
        self.QD_btn.clicked.connect(self.set_slot)
        self.Cancel_btn.clicked.connect(self.cancel_slot)
    
    def set_slot(self):
        if self.lineEdit.text() != "":
            self.setSignal.emit(1)
        else: self.setSignal.emit(0)

    def cancel_slot(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Info_Dialog()
    window.show()
    sys.exit(app.exec_())