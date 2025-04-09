import sys
from PyQt5.QtWidgets import QWidget, QApplication, QMainWindow
from ui_MainWindow import Ui_ECGB_Window


class ECGB_Window(QMainWindow, Ui_ECGB_Window):
    def __init__(self):
        super(ECGB_Window, self).__init__()
        self.setupUi(self)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    ECGB_Window = ECGB_Window()
    ECGB_Window.show()
    sys.exit(app.exec_())
