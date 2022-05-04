import turtle
from turtle import Turtle
import time


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.color("black")
        self.font = ("courier", 20, 'normal')
        self.score = 0
        self.hideturtle()
        self.level = 0
        # Will display `Level: 1` on screen
        self.change_level()

    def game_over(self):
        for _ in range(3):
            self.color('red')
            self.write("GAME OVER", align="center", font=self.font)

    def print(self, message):
        self.clear()
        self.goto(0, 0)
        self.write(message, align="center", font=self.font)
        time.sleep(1)
        self.clear()

    def add_point(self):
        self.score += 1

    def change_level(self):
        self.clear()
        self.color("white")
        self.level += 1
        self.goto(-325, 250)
        self.write(f"Level:{self.level}", font=self.font)

