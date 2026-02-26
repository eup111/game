import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from config import *
from PyQt6.QtGui import QPainter, QPixmap
from PyQt6.QtGui import QPainter, QColor
from PyQt6.QtCore import QRect
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("PyQt6 按钮示例")
        self.setGeometry(100, 100, 800, 600)  # 设置窗口位置和大小

        # 创建一个按钮
        self.button = QPushButton("点击我", self)
        self.button.setGeometry(0, 0, 100, 50)  # 设置按钮位置和大小
        self.button.clicked.connect(self.on_button_clicked)  # 连接点击事件处理器
        self.update()

    def on_button_clicked(self):
        QMessageBox.information(self, "消息", "你点击了按钮！")
    def paintEvent(self, event):
        target = QRect(100, 100, 20, 20)
        painter = QPainter(self)
        painter.fillRect(400,100,4,4, QColor("green"))
        painter.drawPixmap(target, QPixmap(r"d:\python\project\game\img\snakehead.png"))



if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())
