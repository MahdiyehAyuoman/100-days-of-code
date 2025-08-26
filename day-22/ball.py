from turtle import Turtle, Screen


class Ball(Turtle):
    def __init__(self, x_pos, y_pos):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.color('white')
        self.goto(x_pos, y_pos)
        self.x_move = 10
        self.y_move = 10


    def go_to_start(self):
        y_pos = self.ycor() + self.y_move
        x_pos = self.xcor() + self.x_move
        self.goto(x_pos, y_pos)

    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset_position(self):
        self.goto(0,0)
        self.bounce_x()
