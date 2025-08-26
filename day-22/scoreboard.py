from turtle import Turtle


FONT = ("Courier", 30, "bold")
ALIGHNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.hideturtle()
        self.right_score = 0
        self.left_score = 0
        self.define_score()
    
    def define_score(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font=(FONT))
        self.goto(100, 200)
        self.write(self.right_score, align="center", font=(FONT))
                   

    def sum_score_left(self):
        self.left_score += 1
        self.define_score()


    def sum_score_right(self):
        self.right_score += 1
        self.define_score()


