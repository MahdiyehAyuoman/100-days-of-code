from turtle import Turtle, Screen
import random

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title="Make your bet", prompt="Who will win the race? Enter a color:").lower()
## make 6 turtle for the game
color_list = ['blue', 'green', 'red', 'yellow', 'purple', 'orange']

## check if user_bet is valid
if user_bet not in color_list:
    user_bet = screen.textinput(title="Make your bet", prompt="You did not enter a valid color. Enter a color:").lower()

def make_turtle(color,x,y):
    new_turtle = Turtle()
    new_turtle.shape("turtle")
    new_turtle.color(color)
    new_turtle.penup()
    new_turtle.goto(x,y)

    return new_turtle

jim = make_turtle(color_list[0], -230, 100)
mahi = make_turtle(color_list[1], -230, 50)
tim = make_turtle(color_list[2], -230, 0)
pam = make_turtle(color_list[3], -230, -50)
kobi = make_turtle(color_list[4], -230, -100)
kim = make_turtle(color_list[5], -230, -150)

turtles_gamer = [jim, mahi, tim, pam, kobi, kim]
is_end = True
while is_end:
    for turtle in turtles_gamer:
        if turtle.xcor() > 230:
            is_end = False
            winning_turtle_color = turtle.color()[0]
            print(winning_turtle_color)

            if user_bet == winning_turtle_color:
                print(f"You win!")
            else:
                print(f"You lose. The winning color was {winning_turtle_color}.")
            break
        move_distance = random.randint(0, 10)
        turtle.forward(move_distance)

screen.exitonclick()
