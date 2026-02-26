from PyQt6.QtCore import  pyqtSignal,QObject
from src.config import X_max,Y_max
class Snake(QObject):
    dead_singal = pyqtSignal()
    def __init__(self,x,y):
        super().__init__() 
        #x,y为蛇的头部
        self.x = x
        self.y = y
        #记录身体的坐标
        self.body = [(x,y)]
        #记录长度
        self.length=1
        #朝向
        self.direction = [0]
        #存活
        self.islive=1
       

    def add_body(self,direction,x,y):
        #0 1 2 3 分别代表上右下左 x,y上一个body的坐标 direction上一个body的朝向
        if direction==0:
            x_tail,y_tail = x,y-1
        elif direction==1:
            x_tail,y_tail = x+1,y
        elif direction==2:
            x_tail,y_tail = x,y+1
        else:
            x_tail,y_tail = x-1,y
        return (x_tail,y_tail)   
                 
    def eat(self):
        self.length +=1
        self.body.append(self.add_body(self.direction[-1],self.body[-1][0],self.body[-1][1]))
        self.direction.append(self.direction[-1]) 

    def move(self,direction,step):
        #移动蛇
        if direction==0:
            self.y -=step
        elif direction==1:
            self.x +=step
        elif direction ==2:
            self.y +=step
        else:
            self.x -=step
        #检查是否碰到边界    
        self.is_dead()
        if self.islive == 0:
            self.dead_singal.emit()
            return     
        #修改头部之后在改变身体
        del self.body[-1]
        self.body.insert(0,(self.x,self.y))
        del self.direction[-1]
        self.direction.insert(0,direction)    

    def is_dead(self):
        #检查是否碰到边界
        if (self.x>0 and self.x<X_max) and (self.y>0 and self.y<Y_max):
            return 
        self.islive=0
        #
      


