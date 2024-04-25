from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("black")
        self.penup()
        self.hideturtle()
        self.goto(-210, 260)
        self.write(f"Score : {self.score}", align="Center", font=("courier", 12, "normal"))

    def write_score(self):
        self.clear()
        self.write(f"Score : {self.score}", align="Center", font=("courier", 24, "normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(f"GAME OVER", align="Center", font=("courier", 50, "normal"))
