from turtle import Screen
import time
from snake import Snake
from food import Food
from scoreboard import ScoreBoard



FONT = ("Courier", 16, "bold")
ALIGHNMENT = "center"

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)

snake = Snake()
food = Food()
scorebord = ScoreBoard()

screen.listen()
screen.onkey(snake.turn_up, "Up")
screen.onkey(snake.turn_down, "Down")
screen.onkey(snake.turn_left, "Left")
screen.onkey(snake.turn_right, "Right")

game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    snake.move_snake()

    # Detect collision with food
    if snake.segments[0].distance(food) < 15:
        food.food_move()
        snake.extend()
        scorebord.sum_score()

    # Detect collision with wall
    if snake.segments[0].xcor() > 280 or snake.segments[0].xcor() < -280 or snake.segments[0].ycor() > 280 or snake.segments[0].ycor() < -280:
        game_is_on = False
        scorebord.game_over()
    
    # Detect collision with tail
    for segment in snake.segments[1:]:
        if snake.segments[0].distance(segment) < 10 and snake.segments[1:]:
            game_is_on = False
            scorebord.game_over()




screen.exitonclick()