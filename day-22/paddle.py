from turtle import Turtle


class Paddle(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('square')
        self.penup()
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.color('white')
        self.goto(x_pos, y_pos)


    def up(self):
        y_pos = self.ycor() + 20
        self.goto(self.xcor(), y_pos)

    def down(self):
        y_pos = self.ycor() - 20
        self.goto(self.xcor(), y_pos)