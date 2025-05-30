COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 5

from turtle import Turtle
import random


class CarManager:
    def __init__(self):
        self.carsList = []
        self.basic_move = STARTING_MOVE_DISTANCE

    def try_spawn_car(self):
        num = random.randint(1, 6)
        if num == 6:
            self.carsMake()

    def carsMake(self):
        car = Turtle()
        car.shape("square")
        car.penup()
        car.setheading(180)
        car.color(random.choice(COLORS))
        y = random.randint(-250, 250)
        car.goto(300, y)
        car.shapesize(stretch_wid=1, stretch_len=2)
        self.carsList.append(car)

    def carMove(self):
        for car in self.carsList:
            car.forward(self.basic_move)

    def moveIncrement(self):
        self.basic_move += MOVE_INCREMENT
