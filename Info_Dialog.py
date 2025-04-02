import sys
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
from PyQt5.QtCore import *

from Info_Dialog_ui import Ui_Info_Dialog

class Info_Dialog(QDialog, Ui_Info_Dialog):
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
        pass

    def cancel_slot(self):
        self.close()

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Info_Dialog()
    window.show()
    sys.exit(app.exec())