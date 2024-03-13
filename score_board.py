from turtle import Turtle
FONT = ("Courier", 24, "normal")
Final_FONT = ("Courier", 48, "normal")


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.hideturtle()
        self.color("white")
        self.goto(-220, 250)
        self.score = -5
        self.update_score()

    def update_score(self):
        self.clear()
        self.score += 5
        self.write(f"Score: {self.score}", align="center", font=FONT)
        if self.score == 25:
            self.goto(0, 0)
            self.write("You Won!\nClick on screen to exit", align="center", font=FONT)

    def game_over(self):
        self.goto(0, 0)
        self.write("GAME OVER!\nClick on screen to exit", align="center", font=FONT)
