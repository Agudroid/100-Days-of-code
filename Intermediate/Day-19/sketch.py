import turtle
from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forwards():
    tim.forward(10)


def move_backwards():
    tim.backward(10)


def clockwise():
    new_heading = tim.heading() - 10
    tim.setheading(new_heading)


def counter_clockwise():
    new_heading = tim.heading() + 10
    tim.setheading(new_heading)


def clear():
    tim.clear()
    tim.penup()
    tim.home()
    tim.pendown()


def move_turtle():
    turtle.onkeypress(key="space", fun=move_forwards)
    turtle.onkeypress(key="w", fun=move_forwards)
    turtle.onkeypress(key="s", fun=move_backwards)
    turtle.onkeypress(key="a", fun=counter_clockwise)
    turtle.onkeypress(key="d", fun=clockwise)
    turtle.onkeypress(key="c", fun=clear)


screen.listen()
move_turtle()
screen.exitonclick()
