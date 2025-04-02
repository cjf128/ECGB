import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from CK_Dialog_ui import Ui_CK_Dialog


class CK_Dialog(QDialog, Ui_CK_Dialog):
    def __init__(self, parent=None):
        super(CK_Dialog, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setFixedSize(300, 300)
        
        self.config()

    def config(self):
        self.Open_btn.clicked.connect(self.open_slot)
        self.Cancel_btn.clicked.connect(self.cancel_slot)

    def open_slot(self):
        pass

    def cancel_slot(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = CK_Dialog()
    window.show()
    sys.exit(app.exec())