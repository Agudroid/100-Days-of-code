from turtle import Turtle


class Scoreboard(Turtle):
    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = self.read_highscore()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.goto(0, 260)
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="Center", font=("courier", 24, "normal"))

    def update_scoreboard(self):
        self.clear()
        self.write(f"Score : {self.score} High Score : {self.high_score}", align="Center", font=("courier", 24, "normal"))

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("db.txt", mode="w") as file:
                file.write(str(self.high_score))
        self.score = 0
        self.update_scoreboard()

    def read_highscore(self):
        high_score = 0
        with open("db.txt", mode="r") as file:
            content = file.read()
            if content:
                high_score = int(content)

        return high_score
