from turtle import Turtle


FONT = ("Courier", 16, "bold")
ALIGHNMENT = "center"

class ScoreBoard(Turtle):
    def __init__(self):
        super().__init__()
        self.color('white')
        self.penup()
        self.setposition(0, 270)
        self.score = 0
        self.write(f"Score: {self.score}", align= ALIGHNMENT, font=FONT)
        self.hideturtle()
        self.sum_score()
    
    def sum_score(self):
        self.clear()
        self.write(f"Score: {self.score}", align=ALIGHNMENT, font=FONT)
        self.score+=1

    def game_over(self):
        self.penup()
        self.setposition(0, 0)
        self.write(f"Game Over", align=ALIGHNMENT, font=FONT)



