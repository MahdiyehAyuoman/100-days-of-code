import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard

STARTING_POSITION = (0, -280)

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)

turtle_player = Player()
cars = CarManager()
score = Scoreboard()

screen.listen()
screen.onkey(turtle_player.move, "Up")

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    cars.generate_cars()
    cars.move_cars()
    #Detect collision with car
    for car in cars.all_cars:
        if car.distance(turtle_player) < 20:
            game_is_on = False
            score.game_over()

    if turtle_player.level_up() == True:
        score.level_up()
        cars.speed()

screen.exitonclick()

          
