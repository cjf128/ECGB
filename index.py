from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

import serial

from CK_Dialog import CK_Dialog
from ECGB import Ui_ECGB_Window
from Info_Dialog import Info_Dialog

class ECGB_Window(QMainWindow, Ui_ECGB_Window):
    def __init__(self):
        super(ECGB_Window, self).__init__()
        self.setupUi(self)
        self.setWindowIcon(QIcon('./icons/ECGB.png'))
        self.setWindowTitle('ECGB')
        self.setFixedSize(1200, 800)

        self.ser = serial.Serial()

        self.config()

    def config(self):
        self.CK_btn.clicked.connect(self.CK_slot)
        self.XX_btn.clicked.connect(self.Info_slot)

    def CK_slot(self):
        self.CK_Dialog = CK_Dialog()
        self.CK_Dialog.setWindowModality(Qt.ApplicationModal) 
        self.CK_Dialog.show()
        self.CK_Dialog.exec_()
    
    def Info_slot(self):
        self.Info_Dialog = Info_Dialog()
        self.Info_Dialog.setWindowModality(Qt.ApplicationModal) 
        self.Info_Dialog.show()
        self.Info_Dialog.exec_()


if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = ECGB_Window()
    window.show()
    sys.exit(app.exec_())
