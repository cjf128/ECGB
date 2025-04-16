from PyQt5.QtWidgets import QApplication, QMainWindow, QPushButton, QTextEdit, QUndoStack, QUndoCommand
from PyQt5.QtGui import QTextCursor

# 自定义一个撤销命令（例如文本插入操作）
class InsertTextCommand(QUndoCommand):
    def __init__(self, text_edit, text, cursor_pos):
        super().__init__()
        self.text_edit = text_edit
        self.text = text
        self.cursor_pos = cursor_pos

    def undo(self):
        # 撤销操作：删除插入的文本
        cursor = self.text_edit.textCursor()
        cursor.setPosition(self.cursor_pos)
        cursor.movePosition(QTextCursor.Right, QTextCursor.KeepAnchor, len(self.text))
        cursor.removeSelectedText()
        self.text_edit.setTextCursor(cursor)

    def redo(self):
        # 重做操作：重新插入文本
        cursor = self.text_edit.textCursor()
        cursor.setPosition(self.cursor_pos)
        cursor.insertText(self.text)
        self.text_edit.setTextCursor(cursor)

class CustomUndoRedoDemo(QMainWindow):
    def __init__(self):
        super().__init__()
        self.undo_stack = QUndoStack()  # 创建撤销堆栈
        self.initUI()

    def initUI(self):
        self.setWindowTitle("自定义撤销/重做示例")
        self.setGeometry(100, 100, 600, 400)

        # 文本编辑区域
        self.text_edit = QTextEdit(self)
        self.setCentralWidget(self.text_edit)

        # 添加按钮
        btn_insert = QPushButton("插入文本", self)
        btn_insert.clicked.connect(self.insert_text)
        btn_insert.move(10, 10)

        btn_undo = QPushButton("撤销", self)
        btn_undo.clicked.connect(self.undo_stack.undo)
        btn_undo.move(100, 10)

        btn_redo = QPushButton("重做", self)
        btn_redo.clicked.connect(self.undo_stack.redo)
        btn_redo.move(190, 10)

    def insert_text(self):
        text = "Hello PyQt5"
        cursor = self.text_edit.textCursor()
        pos = cursor.position()
        command = InsertTextCommand(self.text_edit, text, pos)
        self.undo_stack.push(command)  # 将命令推入堆栈

if __name__ == "__main__":
    app = QApplication([])
    window = CustomUndoRedoDemo()
    window.show()
    app.exec_()