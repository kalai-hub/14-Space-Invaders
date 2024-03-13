# enemy_ship.py
from turtle import Turtle
import random


class Enemy(Turtle):
    def __init__(self):
        super().__init__()
        self.color("red")
        self.shape("circle")
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.penup()
        self.speed(0)
        self.setheading(270)
        x = random.randint(-350, 350)
        y = random.randint(180, 280)
        self.setposition(x, y)
        self.enemy_speed = 0.2

    def move_enemy(self):

        enemy_x = self.xcor()
        enemy_x += self.enemy_speed
        self.setx(enemy_x)

        # Move the enemy back and down
        if self.xcor() > 380:
            # Move all enemies down
            y = self.ycor()
            y -= 40
            self.sety(y)
            # Change enemy direction
            self.enemy_speed *= -1

        if self.xcor() < -380:
            # Move all enemies down
            y = self.ycor()
            y -= 40
            self.sety(y)
            # Change enemy direction
            self.enemy_speed *= -1

    def remove_enemy(self):
        self.setposition(0, -300)
