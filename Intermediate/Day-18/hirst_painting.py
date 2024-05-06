import colorgram
from turtle import Turtle, Screen
from random import *


def extract_colors():
    colors = colorgram.extract('images.jpg', 16)
    rgb_colors = []
    for color in colors:
        r = color.rgb.r
        g = color.rgb.g
        b = color.rgb.b
        new_color = (r, g, b)
        rgb_colors.append(new_color)
    return rgb_colors


timmy = Turtle()
screen = Screen()
screen.setup(700, 700)
screen.bgcolor("black")
screen.colormode(255)


color_list = extract_colors()
timmy.hideturtle()
timmy.penup()
timmy.setheading(225)
timmy.forward(300)
timmy.setheading(0)
timmy.speed('fastest')
for _ in range(10):

    for _ in range(10):
        timmy.pendown()
        timmy.dot(20, choice(color_list))
        timmy.penup()
        timmy.forward(50)

    timmy.setheading(90)
    timmy.forward(50)
    timmy.setheading(180)
    timmy.forward(500)
    timmy.setheading(0)
screen.exitonclick()

