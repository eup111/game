import random
from src.config import X_max,Y_max
class Food:
    def __init__(self,x,y):
        self.x = x
        self.y = y
    def generate(self):
        self.x = random.randint(0,X_max)
        self.y = random.randint(0,Y_max)