from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



snake = Snake()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.6)

    snake.move_snake()





screen.exitonclick()
