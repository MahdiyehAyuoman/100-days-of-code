import colorgram
from turtle import Turtle, Screen
import turtle as t
import random



# Extract 20 colors from painting project image.
colors = colorgram.extract('image.jpg', 20)
color_list = []

for color in colors:
    tuple_colors = ()
    tuple_colors = list(tuple_colors)
    red = color.rgb.r
    green = color.rgb.g
    blue = color.rgb.b

    tuple_colors.append(red)
    tuple_colors.append(green)
    tuple_colors.append(blue)

    tuple_colors = tuple(tuple_colors)

    color_list.append(tuple_colors)

print(color_list)

jim = Turtle()
screen = Screen()
## Settings for using pencolor and rgb colors
screen.colormode(1)
screen.colormode(255)
screen.screensize(10, 10)


jim.speed('fast')
jim.penup()
jim.hideturtle()
jim.goto(-220, -250)

color_list = [(202, 164, 110), (240, 245, 241), (236, 239, 243), (149, 75, 50), 
              (222, 201, 136), (53, 93, 123), (170, 154, 41), (138, 31, 20), 
              (134, 163, 184),(197, 92, 73), (47, 121, 86), (73, 43, 35), (145, 178, 149), 
              (14, 98, 70), (232, 176, 165), (160, 142, 158), (54, 45, 50), (101, 75, 77)]

def change_color():
    jim.pencolor(random.choice(color_list))

def move():
    for step in range(10):
        jim.dot(20)
        change_color()
        jim.penup()
        jim.forward(50)
        
def turn_left():
    jim.left(90)
    jim.forward(50)
    jim.left(90)
    jim.forward(50)


    
def turn_right():
    jim.right(90)
    jim.forward(50)
    jim.right(90)
    jim.forward(50)

for i in range(5):
    move()
    turn_left()
    move()
    turn_right()
    


screen.exitonclick()
