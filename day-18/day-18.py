from turtle import Turtle, Screen
import turtle as t
import random


jim = Turtle()
t.colormode(255)
jim.shape('turtle')
jim.color('hotpink4')

########### Challenge 1 - Draw Square Challenge ########
def draw_square(step, angle):
    jim.forward(step)
    jim.right(angle)
    jim.forward(step)
    jim.right(angle)
    jim.forward(step)
    jim.right(angle)
    jim.forward(step)

draw_square(150, 90)

########### Challenge 2 - Draw Dashe Line ########
for step in range(15):
    jim.forward(10)
    jim.color('white')
    jim.forward(10)
    jim.color('hotpink4')


########### Challenge 3 - Draw Shapes ########
color_list = ['cornflower blue', 'medium spring green', 'firebrick', 'slate blue', 'saddle brown', 'midnight blue', 'gold']

## Function for calculate angle for each shape
def calculate_angle(sides):
    angle = 360 // sides
    return angle

## Function for select random color each time
def change_color():
    jim.color(random.choice(color_list))

## Function for draw each shape
def draw_shape(side):
    for i in range(side):
        angle = calculate_angle(side)
        jim.forward(150)
        jim.right(angle)


## Triangle
change_color()
draw_shape(3)

# ## Square
change_color()
draw_shape(4)

# ## Pentagon
change_color()
draw_shape(5)

# ## Hexagon
change_color()
draw_shape(6)

## Heptagon
change_color()
draw_shape(7)


## Octagon
change_color()
draw_shape(8)

## Nonagon
change_color()
draw_shape(9)

## Decagon
change_color()
draw_shape(10)



########### Challenge 4 - Draw A Random Walk ########
jim.pensize(10)
jim.speed('fast')

distance = [15, 20, 25, 30]
angle = [45, 90, 180, 360]

for step in range(50):
    change_color()
    jim.forward(random.choice(distance))
    jim.right(random.choice(angle))


########### Challenge 5 - Random Color RGB ########
def random_color():
    r = random.randint(0, 255)
    g = random.randint(0, 255)
    b = random.randint(0, 255)
    color = (r, g, b)
    return color


for step in range(50):
    jim.color(random_color())
    jim.forward(random.choice(distance))
    jim.right(random.choice(angle))


########### Challenge 6 - Draw Spirograph ########
jim.speed('fastest')

for step in range(40):
    jim.color(random_color())
    jim.circle(60)
    position = jim.heading()
    jim.setheading(position + 10)



screen = Screen()
screen.exitonclick()