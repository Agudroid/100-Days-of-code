import turtle
from turtle import Turtle, Screen
import random

timmy = Turtle()
timmy.speed(100)

screen = Screen()
screen.colormode(255)

for i in range(0, 360, 10):
    timmy.color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )

    timmy.setheading(i)
    timmy.circle(100)

screen.exitonclick()
