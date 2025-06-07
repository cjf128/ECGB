import os
import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

from ui_Load_Dialog import Ui_Load_Dialog



class Load_Dialog(QDialog, Ui_Load_Dialog):
    setSignal = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
        self.config()
    
    def config(self):
        self.btnLoad.clicked.connect(self.load_slot)
        self.btnCancel.clicked.connect(self.cancel_slot)
        self.btnSearch.clicked.connect(self.search_slot)
 
    def load_slot(self):
        path = self.ledtPath.text()
        self.setSignal.emit(path)

        self.close()
    
    def cancel_slot(self):
        self.close()

    def search_slot(self):
        load_path, _ = QFileDialog.getOpenFileName(self, '打开文件', os.getcwd(), "Text Files(*.txt)")
        if load_path:
            self.ledtPath.setText(load_path)


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Load_Dialog()
    window.show()
    sys.exit(app.exec_())