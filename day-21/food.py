from turtle import Turtle
import random

class MyTurtleClass(Turtle):
    def __init__(self):
        super().__init__()

class Food(MyTurtleClass):
    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_len=0.5, stretch_wid=0.5)
        self.color('red')
        self.speed('fastest')
        self.food_move()

    def food_move(self):
        x = random.randint(-275, 275)
        y = random.randint(-275, 275)
        self.goto(x, y)







