from turtle import Turtle


class Ball(Turtle):
    def __init__(self):
        super().__init__()
        self.color("White")
        self.shape("circle")
        self.penup()
        self.shapesize(stretch_wid=1, stretch_len=1)
        self.goto(0, 0)
        self.move_speed = 0.1
        self.x_move = 10
        self.y_move = 10

    def move(self):

        new_x = self.xcor() + self.x_move
        new_y = self.ycor() + self.y_move

        self.goto(new_x, new_y)

    def bounce(self):

        self.y_move *= -1

    def retrieve(self):

        self.x_move *= -1
        self.move_speed *= 0.9

    def reset(self):
        self.move_speed = 0.1
        self.goto(0, 0)
