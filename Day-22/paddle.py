from turtle import Turtle


class Paddle(Turtle):

    def __init__(self, position):
        super().__init__()
        self.shape("square")
        self.color("white")
        self.shapesize(stretch_wid=5, stretch_len=1)
        self.penup()
        self.score = 0
        self.__create_score__(position)
        if position == "left":
            self.goto(-380, 0)
        elif position == "right":
            self.goto(380, 0)

    def move_up(self):
        new_y = self.ycor()
        if new_y <= 230:
            new_y += 20
        self.goto(self.xcor(), new_y)

    def move_down(self):
        new_y = self.ycor()
        if new_y >= -230:
            new_y -= 20
        self.goto(self.xcor(), new_y)

    def write_score(self):
        self.scoreboard.clear()
        self.scoreboard.write(f"Score : {self.score}", align="Center", font=("courier", 12, "normal"))

    def __create_score__(self, position):
        x = 300
        if position == "left":
            x *= -1
        self.scoreboard = Turtle()
        self.scoreboard.penup()
        self.scoreboard.color("white")
        self.scoreboard.goto(x, 260)
        self.scoreboard.hideturtle()
        self.scoreboard.write(f"Score : {self.score}", align="Center", font=("courier", 12, "normal"))

