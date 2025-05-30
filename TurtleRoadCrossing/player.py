STARTING_POSITION = (0, -280)
MOVE_DISTANCE = 10
FINISH_LINE_Y = 280

from turtle import Turtle


class Player(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.shape("turtle")
        self.color("black")
        self.setheading(90)
        self.go_to_starting_position()

    # up method
    def up(self):
        if self.ycor() < 290:
            y = self.ycor()
            self.sety(y + MOVE_DISTANCE)

    # down method
    def down(self):
        if self.ycor() > -280:
            y = self.ycor()
            self.sety(y - MOVE_DISTANCE)

    def go_to_starting_position(self):
        self.goto(STARTING_POSITION)

    def is_finish_line_pass(self):
        if self.ycor() > FINISH_LINE_Y:
            return True
        else:
            return False
