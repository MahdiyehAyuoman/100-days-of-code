from turtle import Turtle
STARTING_POSITION = (0, -280)
# MOVE_DISTANCE = 10
MOVE_DISTANCE = 20
FINISH_LINE_Y = 280


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.shape('turtle')
        self.left(90)
        self.color('green')
        self.penup()
        self.goto(STARTING_POSITION)
    
    def move(self):
        y_pos = self.ycor() + MOVE_DISTANCE
        self.goto(self.xcor(), y_pos)
        # self.forward(MOVE_DISTANCE)

    def level_up(self):
        if self.ycor() > FINISH_LINE_Y:
            self.goto(STARTING_POSITION)
            return True
