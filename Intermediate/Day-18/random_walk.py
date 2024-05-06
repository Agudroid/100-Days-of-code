from turtle import Turtle, Screen
import random

timmy = Turtle()
screen = Screen()
screen.colormode(255)

movements = [0,90,180,270]
number_of_movements = random.randint(100, 200)
timmy.speed('fastest')
timmy.pensize(15)
for i in range(number_of_movements):

    timmy.color(
        random.randint(0, 255),
        random.randint(0, 255),
        random.randint(0, 255)
    )
    angle = random.choice(movements)

    timmy.setheading(angle)
    timmy.forward(30)

screen.exitonclick()