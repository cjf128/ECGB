import sys
from PyQt5.QtCore import QUrl
from PyQt5.QtWidgets import QApplication, QWidget, QPushButton
from PyQt5.QtMultimedia import QSoundEffect

class Demo(QWidget):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("音效控制示例")
        
        # 初始化QSoundEffect
        self.sound_effect = QSoundEffect()
        self.sound_effect.setSource(QUrl.fromLocalFile("sound.wav"))  # WAV文件路径
        self.sound_effect.setVolume(0.8)  # 音量范围0.0~1.0
        
        # 创建按钮
        self.button = QPushButton("播放音效", self)
        self.button.clicked.connect(self.sound_effect.play)

if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = Demo()
    window.show()
    sys.exit(app.exec_())