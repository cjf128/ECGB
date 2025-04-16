import sys
from PyQt5.QtCore import QPropertyAnimation, QEasingCurve, QRect, Qt, QEvent
from PyQt5.QtWidgets import (QApplication, QMainWindow, QWidget, QVBoxLayout, 
                            QPushButton, QLabel, QGraphicsDropShadowEffect)
from PyQt5.QtGui import QColor

class AnimatedSidebar(QWidget):
    def __init__(self, parent=None):
        super().__init__(parent)
        self.parent = parent
        self.is_visible = False
        self.init_ui()
        self.init_animation()
        
    def init_ui(self):
        self.setFixedWidth(250)
        self.setStyleSheet("""
            background: #2c3e50;
            border-radius: 10px;
            padding: 20px;
        """)
        
        # 添加阴影效果
        self.shadow = QGraphicsDropShadowEffect()
        self.shadow.setBlurRadius(15)
        self.shadow.setColor(QColor(0, 0, 0, 150))
        self.shadow.setOffset(5, 5)
        self.setGraphicsEffect(self.shadow)
        
        layout = QVBoxLayout()
        layout.setAlignment(Qt.AlignTop)
        
        nav_items = ["🏠 首页", "⚙️ 设置", "📚 文档", "📧 联系"]
        for item in nav_items:
            btn = QPushButton(item)
            btn.setStyleSheet("""
                QPushButton {
                    color: #ecf0f1;
                    font-size: 16px;
                    text-align: left;
                    padding: 15px;
                    border-radius: 8px;
                    background: transparent;
                }
                QPushButton:hover {
                    background: #34495e;
                }
            """)
            layout.addWidget(btn)
        
        self.setLayout(layout)
        self.move(-self.width(), 0)  # 初始位置在左侧外部
        
    def init_animation(self):
        self.animation = QPropertyAnimation(self, b"geometry")
        self.animation.setDuration(400)
        self.animation.setEasingCurve(QEasingCurve.OutCubic)

    def toggle(self):
        if self.is_visible:
            self.hide_sidebar()
        else:
            self.show_sidebar()

    def show_sidebar(self):
        if not self.is_visible:
            self.is_visible = True
            self.raise_()  # 确保显示在最上层
            self.animation.setStartValue(QRect(-self.width(), 0, self.width(), self.parent.height()))
            self.animation.setEndValue(QRect(0, 0, self.width(), self.parent.height()))
            self.animation.start()

    def hide_sidebar(self):
        if self.is_visible:
            self.is_visible = False
            self.animation.setStartValue(QRect(0, 0, self.width(), self.parent.height()))
            self.animation.setEndValue(QRect(-self.width(), 0, self.width(), self.parent.height()))
            self.animation.start()

class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.init_ui()
        self.init_sidebar()
        
    def init_ui(self):
        self.setWindowTitle("Modern Sidebar Demo")
        self.setGeometry(100, 100, 1200, 800)
        self.setStyleSheet("background: #f5f6fa;")

        self.main_content = QLabel("主内容区域")
        self.main_content.setAlignment(Qt.AlignCenter)
        self.main_content.setStyleSheet("font-size: 24px; color: #7f8c8d;")
        self.setCentralWidget(self.main_content)

        # 汉堡菜单按钮
        self.menu_btn = QPushButton("☰", self)
        self.menu_btn.setFixedSize(45, 45)
        self.menu_btn.move(20, 20)
        self.menu_btn.setStyleSheet("""
            QPushButton {
                background: #3498db;
                color: white;
                border-radius: 22px;
                font-size: 24px;
                border: 2px solid #2980b9;
            }
            QPushButton:hover {
                background: #2980b9;
            }
        """)
        self.menu_btn.clicked.connect(self.toggle_sidebar)

    def init_sidebar(self):
        self.sidebar = AnimatedSidebar(self)
        self.installEventFilter(self)  # 安装事件过滤器
        
    def toggle_sidebar(self):
        self.sidebar.toggle()
        self.menu_btn.setText("✕" if self.sidebar.is_visible else "☰")

    def eventFilter(self, obj, event):
        # 点击侧边栏外部时关闭
        if event.type() == QEvent.MouseButtonPress:
            if self.sidebar.is_visible:
                if not self.sidebar.geometry().contains(event.pos()):
                    self.sidebar.hide_sidebar()
                    self.menu_btn.setText("☰")
        return super().eventFilter(obj, event)

    def resizeEvent(self, event):
        self.sidebar.setFixedHeight(self.height())
        super().resizeEvent(event)

if __name__ == '__main__':
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec_())