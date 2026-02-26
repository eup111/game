from PyQt6.QtWidgets import  QMainWindow, QPushButton,QWidget,QLabel
from PyQt6.QtWidgets import QVBoxLayout,QHBoxLayout,QSpacerItem,QSizePolicy
from PyQt6.QtCore import Qt,pyqtSignal
from .config import X_max,Y_max,bk1_path,title_path
from PyQt6.QtGui import QIcon
class Playmenu(QMainWindow):
    play_singal = pyqtSignal()
    
    def __init__(self):
        super().__init__()
        self.setFixedSize(X_max,Y_max)#设置窗口大小
        self.setWindowTitle("game")
        self.setWindowIcon(QIcon(title_path))
        self.setStyleSheet(f"""
            QMainWindow {{
                border-image: url({bk1_path}) 0 0 0 0 stretch stretch;
            }}
        """)
        #设置界面
        self.in_btn=QPushButton()
        self.in_btn.setText("start game")
        self.in_btn.setFixedSize(100,50)
        self.in_btn.setStyleSheet("""
        QPushButton {
        font-family: 'Comic Sans MS';
        font-size: 15px;
        font-weight: bold;
        color: green;
        background-color: transparent;
        border: none;
          }
        QPushButton:hover {
        background-color: lightgreen;
        border-radius: 10px;
         }
         """)
        self.hlayout1=QHBoxLayout()#水平布局
        self.sp1 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.sp2 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.hlayout1.addItem(self.sp1)
        self.hlayout1.addWidget(self.in_btn)
        self.hlayout1.addItem(self.sp2)
        #设置标题
        self.hlayout2=QHBoxLayout()#水平布局
        self.label=QLabel()
        self.label.setText("gluttonous snake game ")
        self.label.setSizePolicy(QSizePolicy.Policy.Expanding,QSizePolicy.Policy.Expanding)
        self.label.setAlignment(Qt.AlignmentFlag.AlignCenter)
        self.label.setStyleSheet("font-family:'Comic Sans MS';font-size: 30px; font-weight: bold;color: green;")
        self.sp3 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.sp4 = QSpacerItem(20, 40, QSizePolicy.Policy.Expanding, QSizePolicy.Policy.Minimum)
        self.hlayout2.addItem(self.sp3)
        self.hlayout2.addWidget(self.label)
        self.hlayout2.addItem(self.sp4)
        #设置布局
        container = QWidget()#Widget容器
        self.vlayout = QVBoxLayout()#垂直布局
        container.setLayout(self.vlayout)
        self.vlayout.addLayout(self.hlayout2)
        self.vlayout.addItem(QSpacerItem(20, 150, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.vlayout.addLayout(self.hlayout1)
        self.vlayout.addItem(QSpacerItem(20, 40, QSizePolicy.Policy.Minimum, QSizePolicy.Policy.Minimum))
        self.setCentralWidget(container)
        
        #连接信号
        self.in_btn.clicked.connect(self.int_btn_clicked)
    #点击开始游戏按钮 发出信号 关闭界面
    def int_btn_clicked(self):
        self.play_singal.emit()
        self.close()
        self.deleteLater()
        
        
    
 