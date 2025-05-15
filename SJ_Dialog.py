import sys
from PyQt5.QtWidgets import QApplication, QDialog, QFileDialog
from PyQt5.QtCore import pyqtSignal
from PyQt5.QtGui import QIcon

from ui_SJ_Dialog import Ui_SJ_Dialog



class SJ_Dialog(QDialog, Ui_SJ_Dialog):
    setSignal = pyqtSignal(str)
    def __init__(self, parent=None):
        super().__init__(parent)
        self.setupUi(self)
        self.setWindowIcon(QIcon('./ECGB.ico'))
        self.config()
    
    def config(self):
        self.btnSave.clicked.connect(self.save_slot)
        self.btnCancel.clicked.connect(self.cancel_slot)
        self.btnSearch.clicked.connect(self.search_slot)
 
    def save_slot(self):
        path = self.ledtPath.text()
        self.setSignal.emit(path)

        self.close()
    
    def cancel_slot(self):
        self.close()

    def search_slot(self):
        save_path = QFileDialog.getExistingDirectory(self, "选择保存路径", "./")
        if save_path:
            self.ledtPath.setText(save_path)



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = SJ_Dialog()
    window.show()
    sys.exit(app.exec_())