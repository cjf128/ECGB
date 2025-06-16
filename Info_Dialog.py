import sys
from PySide2.QtWidgets import QDialog, QApplication
from PySide2.QtGui import QIcon
from PySide2.QtCore import Signal

from ui_Info_Dialog import Ui_Info_Dialog

class Info_Dialog(QDialog, Ui_Info_Dialog):
    setSignal = Signal(bool)

    def __init__(self, parent=None):
        super(Info_Dialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
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