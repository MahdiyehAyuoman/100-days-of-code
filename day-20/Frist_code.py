
from turtle import Turtle, Screen
import time
from snake import Snake

screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("Snake Game")
screen.tracer(0)



# ## Frist try to make a snake
# # s_1 = Turtle()
# # s_1.color("white")
# # s_1.shape("square")

# # s_2 = Turtle()
# # s_2.color("white")
# # s_2.shape("square")
# # s_2.goto(-20,0)

# # s_3 = Turtle()
# # s_3.color('white')
# # s_3.shape("square")
# # s_3.goto(-40,0)

# define a function for make the snake 
x_y_posiotion = [(0,0), (-20,0), (-40,0)]
segment = []
def make_snake(x_y_posiotion):
    for posotion in x_y_posiotion:
        snake = Turtle()
        snake.penup()
        snake.color("white")
        snake.shape("square")
        snake.goto(posotion)
        segment.append(snake)

make_snake(x_y_posiotion)


# Move Snake
game_is_on = True
while game_is_on:
    screen.update()
    time.sleep(0.1)
    for seg_num in range(len(segment)-1, 0, -1):
        new_x = segment[seg_num - 1].xcor()
        new_y = segment[seg_num - 1].ycor()
        segment[seg_num].goto(new_x, new_y)
    segment[0].forward(20)
    # segment[0].right(90)