from turtle import Turtle
import os

ALIGNMENT = "center"
FONT = ("Courier", 24, "normal")

path = os.path.abspath(os.path.dirname(__file__))

path = path+"\high_score.txt"


def read_high_score():
    high_score = 0
    try:
        with open(path) as file:
            high_score = int(file.read())
    except FileNotFoundError:
        return 0
    return high_score


class Scoreboard(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = read_high_score()
        self.color("white")
        self.penup()
        self.goto(0, 270)
        self.hideturtle()
        self.update_scoreboard()

    def update_scoreboard(self):
        self.write(f"Score: {self.score} High Score:{self.high_score}",
                   align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()

    def reset(self):
        self.clear()
        if self.score > self.high_score:
            self.high_score = self.score
            with open(path, mode="w") as file:
                file.write(str(self.score))
        self.score = 0
        self.update_scoreboard()


# test = Scoreboard()
# hight_score = test.high_score
# print(hight_score)
