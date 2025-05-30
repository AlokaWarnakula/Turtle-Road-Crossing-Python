FONT = ('Comic Sans MS', 20, 'bold')
LOSE = ('Comic Sans MS', 40, 'bold')
ALIGN = 'left'
from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.level = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-230,270)
        self.writingScore()

    def writingScore(self):
        level = self.level
        self.write(f"Level: {level}", move=False, align=ALIGN, font=FONT)

    def addLevel(self):
        self.level += 1
        self.clear()
        self.writingScore()

    def hitCar(self):
        self.goto(0, 0)
        self.write("Turtle Died", move=False, align='center', font=LOSE)

