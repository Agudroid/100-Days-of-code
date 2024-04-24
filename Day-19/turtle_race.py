import random
import turtle
from turtle import Turtle, Screen
from random import randint

screen = Screen()
screen.setup(width=500, height=400)
user_bet = screen.textinput(title='Make your bet', prompt='Which turtle will win the race?: ')
color_list = ['red', 'orange', 'yellow', 'green', 'blue', 'purple']
turtle_list = []
is_race_on = True


def create_turtles():
    y_coord = 100
    while len(color_list) > 0:
        new_turtle = Turtle()
        new_turtle.penup()
        new_turtle.shape('turtle')
        new_turtle.color(color_list[0])
        new_turtle.goto(x=-230, y=y_coord)
        turtle_list.append(new_turtle)
        color_list.pop(0)
        y_coord -= 50


create_turtles()


def run_turtles():

    for turtle_i in turtle_list:
        print(turtle_i.xcor())
        if turtle_i.xcor() > 230:
            winner = turtle_i.pencolor()
            if winner == user_bet:
                print("You´ve won the race")
            else:
                print("You lose")
            return False
        rand_dist = random.randint(0, 10)
        turtle_i.forward(rand_dist)
    return True


while is_race_on:
    is_race_on = run_turtles()

screen.exitonclick()
