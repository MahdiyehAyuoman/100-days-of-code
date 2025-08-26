from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball
import time
from scoreboard import ScoreBoard

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

## Define Paddles from Paddle Class
right_paddle = Paddle(350, 0)
left_paddle = Paddle(-350, 0)


## Define Ball from ball Class
ball = Ball(0, 0)

## Define ScoreBoard from scoreboard Class
score_board = ScoreBoard()

## Move Paddles Up & Down
screen.listen()
screen.onkey(right_paddle.up, "Up")
screen.onkey(right_paddle.down, "Down")
screen.onkey(left_paddle.up, "w")
screen.onkey(left_paddle.down, "s")


game_is_on = True
while game_is_on:

    time.sleep(0.1)
    screen.update()
    ball.go_to_start()

    #Detect collision with wall
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce_y()

    #Detect collision with the paddles
    if ball.distance(right_paddle) < 50 and ball.xcor() > 320:
        ball.bounce_x()

    elif ball.distance(left_paddle) < 50 and ball.xcor() > -320:
        ball.bounce_x()

    #Detect right paddle misses
    if ball.xcor() > 380:
        ball.reset_position()
        score_board.sum_score_left()

    #Detect left paddle misses
    if ball.xcor() < -380:
        ball.reset_position()
        score_board.sum_score_right()


screen.exitonclick()