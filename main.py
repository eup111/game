import sys
from PyQt6.QtWidgets import QApplication, QMainWindow, QPushButton, QMessageBox
from PyQt6.QtGui import QPainter, QColor
from src.snake import Snake
from PyQt6.QtCore import QTimer,Qt
from src.config import step,X_max,Y_max,Defalut_Direction,food_nums,eat_range
from src.food import Food
class MainWindow(QMainWindow):
    def __init__(self):
        super().__init__()
        self.setWindowTitle("game")
        self.setGeometry(100, 100, X_max, Y_max)  # 设置窗口位置和大小
        #设置初始蛇
        self.snake =Snake(X_max//2,Y_max//2)
        #设置初始方向
        self.direction = Defalut_Direction
        #设置食物
        self.foods = []
        for i in range(food_nums):
            food = Food(0,0)
            food.generate()#随机位置
            self.foods.append(food)

        self.snake.dead_singal.connect(self.death)#死亡发出信号 调用death函数

        #方向按钮
        self.button_up = QPushButton("↑", self)
        self.button_right = QPushButton("→", self)
        self.button_down = QPushButton("↓", self)
        self.button_left = QPushButton("←", self)
        self.button_up.setGeometry(0, 0, 50, 50)
        self.button_right.setGeometry(50, 0, 50, 50)
        self.button_down.setGeometry(100, 0, 50, 50)
        self.button_left.setGeometry(150, 0, 50, 50)

        

        self.click()#点按钮改变方向 会朝方向自动移动
        self.timer = QTimer(self)
        self.timer.setInterval(150)
        self.timer.timeout.connect(self.paint_and_check)
        self.timer.start()

    def paint_and_check(self):
        #移动 画蛇和检查死亡
        if self.snake.islive:
            self.snake.move(self.direction, step)
        self.snake.is_dead()#检查是否触发死亡条件
        if self.snake.islive == 0:
            self.timer.stop()
        self.update()#会自动调用paintEvent
        #检查是否吃到食物 不要求坐标重合
        for i in self.foods:
            if(abs(self.snake.x-i.x)<eat_range and abs(self.snake.y-i.y)<eat_range):
                self.snake.eat()
                self.foods.remove(i)

    def set_direction(self,direction):
        #设置方向
        self.direction = direction

    def click(self):
        #按按钮后改变方向
        self.button_up.clicked.connect(lambda:self.set_direction(0))
        self.button_right.clicked.connect(lambda:self.set_direction(1))
        self.button_down.clicked.connect(lambda:self.set_direction(2))
        self.button_left.clicked.connect(lambda:self.set_direction(3))

    def death(self):
        #死亡信息
        QMessageBox.critical(self, "消息", "你死了")

    def paintEvent(self, event):
        #update会自动调用 以x,y为中心画一个方块
        painter = QPainter(self)
        block_size = 4
        half = block_size // 2
        for i,(x,y) in enumerate(self.snake.body):
            painter.fillRect(x-half,y-half,block_size,block_size,QColor("green"))
        #画出食物
        for i in self.foods:
            painter.fillRect(i.x-half,i.y-half,block_size,block_size,QColor("red"))    


if __name__ == "__main__":
    app = QApplication(sys.argv)
    window = MainWindow()
    window.show()
    sys.exit(app.exec())


