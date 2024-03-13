# bullet.py
from turtle import Turtle

bullet_speed = 2


class Bullet(Turtle):
    def __init__(self):
        super().__init__()
        self.color("yellow")
        self.shape("triangle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed(0)
        self.setheading(90)
        self.hideturtle()
        self.next_bullet = True
        self.x = 0
        self.y = 0

    def fire_bullet(self, player):
        if self.next_bullet:
            self.next_bullet = False
            self.x = player.xcor()
            self.y = player.ycor()
            self.setposition(self.x, self.y)
            self.showturtle()
            self.next_bullet = True

    def move_bullet(self):
        if self.ycor() < 350:
            self.y += bullet_speed
            self.setposition(self.x, self.y)
            return True
        if self.ycor() >= 350:
            return False
