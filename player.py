# player.py
from turtle import Turtle

PLAYER_SPEED = 15
class Player(Turtle):
    def __init__(self, coordinates):
        super().__init__()
        self.color("white")
        self.shape("triangle")
        self.shapesize(stretch_wid=2, stretch_len=2)
        self.penup()
        self.setheading(90)
        self.xcoordinates = coordinates[0]
        self.ycoordinates = coordinates[1]
        self.goto(self.xcoordinates, self.ycoordinates)

    def left(self):
        x = self.xcor()
        x -= PLAYER_SPEED
        if x < -280:
            x = -280
        self.setx(x)

    def right(self):
        x = self.xcor()
        x += PLAYER_SPEED
        if x > 280:
            x = 280
        self.setx(x)