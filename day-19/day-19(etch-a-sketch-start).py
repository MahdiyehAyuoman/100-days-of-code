from turtle import Turtle, Screen

jim = Turtle()
screen = Screen()


def move_forwards():
    jim.forward(20)

def move_backwards():
    jim.backward(20)

def move_home():
    jim.home()
    jim.clear()

def clockwise():
    jim.right(10)

def counter_clockwise():
    jim.left(10)

screen.listen()
screen.onkey(key="w", fun=move_forwards)
screen.onkey(key="s", fun=move_backwards)
screen.onkey(key="c", fun=move_home)
screen.onkey(key="d", fun=clockwise)
screen.onkey(key="a", fun=counter_clockwise)

screen.exitonclick()
