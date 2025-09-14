from turtle import Turtle
import os

ALIGNMENT_SCORE = "right"
ALIGNMENT_HIGH_SCORE = "left"
ALIGNMENT = "center"
FONT = ("Courier", 20, "normal")


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.high_score = self.read_highscore()
        self.update_scoreboard()

    def read_highscore(self):
        data_file_path = os.path.join("2. Snake Project Code from Day 21", "data.txt")
        with open(data_file_path, 'r') as file:
            hs = file.read()
            return int(hs)

    def update_scoreboard(self):
        self.write(f"Score: {self.score}", align=ALIGNMENT_SCORE, font=FONT)
        if self.score > self.high_score:
            self.high_score = self.score
        self.write(f"High Score: {self.high_score}", align=ALIGNMENT_HIGH_SCORE, font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()
        data_file_path = os.path.join("2. Snake Project Code from Day 21", "data.txt")
        if self.score > self.high_score:
            self.high_score = self.score
        with open(data_file_path, 'w') as file:
            hs = file.write(f"{self.high_score}")
            return int(hs)
