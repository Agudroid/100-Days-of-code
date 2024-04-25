from turtle import Turtle


class CrossyTurtle(Turtle):
    def __init__(self):
        super().__init__()
        self.penup()
        self.setheading(90)
        self.color('Black')
        self.shape('turtle')
        self.goto(0, -280)

    def move_forward(self):
        self.forward(20)
