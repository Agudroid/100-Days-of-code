from turtle import Turtle,Screen
from random import randint

timmy = Turtle()
screen = Screen()
timmy.shape("arrow")
screen.colormode(255)
for sides in range(3, 11):

    timmy.color(
        randint(0, 255),
        randint(0, 255),
        randint(0, 255)
    )

    rotation = 360/sides
    for j in range(sides+1):
        timmy.forward(100)
        timmy.right(rotation)

screen.exitonclick()
