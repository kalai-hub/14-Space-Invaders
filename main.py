# main.py
from turtle import Screen
from player import Player
from bullet import Bullet
from enemy_ship import Enemy
from score_board import Scoreboard
import threading

screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Breakout")

screen.delay(0)
player = Player((0, -250))

bullet = Bullet()
enemy_obj = []

score_board = Scoreboard()


def fire_bullet():
    global fire
    fire = True
    if not already_fired:
        bullet.fire_bullet(player)


screen.listen()
screen.onkey(player.left, "Left")
screen.onkey(player.right, "Right")
screen.onkeypress(fire_bullet, "space")

game_is_on = True
enemy_created = False
fire = False
already_fired = False
enemy_count = 5

while game_is_on:
    if not enemy_created:
        for i in range(5):
            enemy = Enemy()
            enemy_obj.append(enemy)
        enemy_created = True
    for i in range(len(enemy_obj)):
        enemy_obj[i].move_enemy()

        # Identify collision with bullet

        if enemy_obj[i].distance(bullet) < 25:
            enemy_obj[i].remove_enemy()
            enemy_count -= 1
            score_board.update_score()

        # Identify collision with player

        if enemy_obj[i].distance(player) < 25:
            score_board.game_over()
            game_is_on = False
    if fire:
        already_fired = bullet.move_bullet()
        if not already_fired:
            fire = False
    if enemy_count == 0:
        game_is_on = False

screen.exitonclick()
