from PyQt5.QtCore import *
from PyQt5.QtWidgets import *
from PyQt5.QtGui import *
import sys

from ECGB import Ui_ECGB_Window

class ECGB_Window(QMainWindow, Ui_ECGB_Window):
    def __init__(self):
        super(ECGB_Window, self).__init__()
        self.setupUi(self)
        self.setFixedSize(1200, 800)
        self.config()

    def config(self):
        pass

if __name__ == '__main__':
    QGuiApplication.setAttribute(Qt.AA_EnableHighDpiScaling)
    QGuiApplication.setAttribute(Qt.AA_UseHighDpiPixmaps)
    QGuiApplication.setHighDpiScaleFactorRoundingPolicy(Qt.HighDpiScaleFactorRoundingPolicy.PassThrough)

    app = QApplication(sys.argv)
    window = ECGB_Window()
    window.show()
    sys.exit(app.exec_())
