from turtle import Turtle
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('black')
        self.penup()
        self.hideturtle()
        self.score = 1
        self.define_score()
    
    
    def define_score(self):
        self.clear()
        self.goto(-200, 250)
        self.write(f"Level: {self.score}", align="center", font=(FONT))

    def level_up(self):
        self.score +=1
        self.define_score()

    def game_over(self):
        self.goto(0, 0)
        self.write(f"Game over", align="center", font=(FONT))
