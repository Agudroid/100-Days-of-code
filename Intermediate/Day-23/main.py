import random
import time
from turtle import Screen
from crossy_turtle import CrossyTurtle
from car_manager import CarManager
from scoreboard import Scoreboard

screen = Screen()
screen.title("Crossy Road")
screen.tracer(0)
screen.setup(600, 600)

timmy = CrossyTurtle()
manager = CarManager()
scoreboard = Scoreboard()

screen.listen()
screen.onkeypress(timmy.move_forward, "Up")
screen.colormode(255)


is_game_on = True
number_of_cars = 30
while is_game_on:
    scoreboard.write_score()
    if len(manager.car_list) == 0:
        manager.create_cars(random.randint(0, number_of_cars))
    screen.update()
    time.sleep(0.2)
    manager.move_cars()
    if manager.check_collision(timmy):
        is_game_on = False
        manager.car_list.clear()
        scoreboard.game_over()

    if timmy.ycor() > 260:
        scoreboard.score += 1
        timmy.goto(0, -280)
        manager.clear_cars()
        number_of_cars += 30

    screen.update()
screen.exitonclick()
