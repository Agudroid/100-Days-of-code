from turtle import Turtle
from random import randint


class CarManager(Turtle):

    def create_cars(self, number_of_cars):
        for i in range(number_of_cars):
            car = Turtle()
            car.shape("square")
            car.penup()
            car.color(randint(0, 255), randint(0, 255), randint(0, 255))
            car.goto(randint(-780, -280), randint(-220, 300))
            car.shapesize(stretch_len=1, stretch_wid=0.5)
            self.car_list.append(car)

    def __init__(self):
        super().__init__()
        self.car_list = []
        self.hideturtle()

    def move_cars(self):
        for car in self.car_list:
            car.forward(randint(0, 20))
            if car.xcor() > 280:
                car.goto(-280, car.ycor())

    def check_collision(self, player):
        for car in self.car_list:
            if car.distance(player) < 20:
                return True
        return False

    def clear_cars(self):
        for car in self.car_list:
            car.clear()
        self.car_list.clear()
