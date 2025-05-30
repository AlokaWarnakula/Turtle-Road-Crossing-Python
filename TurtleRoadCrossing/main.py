import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Scoreboard
from road_drawing import RoadDrawer

screen = Screen()
screen.setup(width=600, height=600)
screen.tracer(0)
screen.title("Road Cross")

draw = RoadDrawer()
draw.blockGenerate()
cars = CarManager()
score = Scoreboard()
player = Player()

screen.listen()
screen.onkey(fun=player.up, key="Up")
screen.onkey(fun=player.down, key="Down")

game_is_on = True

while game_is_on:
    time.sleep(0.1)
    screen.update()

    if player.is_finish_line_pass():
        print("player won")
        player.go_to_starting_position()
        cars.moveIncrement()
        score.addLevel()

    cars.try_spawn_car()
    cars.carMove()

    for hitCar in cars.carsList:
        if player.distance(hitCar) < 20:
            score.hitCar()
            game_is_on = False

    for car in cars.carsList:
        if car.xcor() < -300:
            cars.carsList.remove(car)
            car.hideturtle()

screen.exitonclick()
