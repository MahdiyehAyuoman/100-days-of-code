from turtle import Screen, Turtle
from paddle import Paddle

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

paddle = Turtle()
paddle.shape('square')
paddle.penup()
paddle.shapesize(stretch_wid=5, stretch_len=1)
paddle.color('white')
paddle.goto(350, 0)

def up():
    y_pos = paddle.ycor() + 20
    paddle.goto(paddle.xcor(), y_pos)

def down():
    y_pos = paddle.ycor() - 20
    paddle.goto(paddle.xcor(), y_pos)


# paddle_gamer_one = Paddle(350, 0)
# paddle_gamer_two = Paddle(-350, 0)


screen.listen()
screen.onkey(up, "Up")
screen.onkey(down, "Down")

game_is_on = True
while game_is_on:
    screen.update()

screen.exitonclick()