import time
from turtle import Screen, Turtle
from paddle import Paddle
from ball import Ball


def field_line():
    line = Turtle()
    line.penup()
    line.color("white")
    line.hideturtle()
    line.pensize(8)
    line.goto(0, 230)
    line.setheading(270)
    for i in range(12):
        line.pendown()
        line.forward(20)
        line.penup()
        line.forward(25)


screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.tracer(0)

player_paddle = Paddle("right")
computer_paddle = Paddle("left")
ball = Ball()

field_line()

screen.listen()
screen.update()
screen.onkeypress(player_paddle.move_up, "Up")
screen.onkeypress(player_paddle.move_down, "Down")
screen.onkeypress(computer_paddle.move_up, "w")
screen.onkeypress(computer_paddle.move_down, "s")
is_game_on = True
while is_game_on:
    time.sleep(ball.move_speed)
    screen.update()
    ball.move()

    # Detect collision with the top and the bottom
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()

    if player_paddle.distance(ball) <= 20 or computer_paddle.distance(ball) <= 20:
        print("Inside")
        ball.retrieve()

    if ball.xcor() > 380 or ball.xcor() < -380:
        if ball.xcor() > 380:
            computer_paddle.score += 1
            print(computer_paddle.score)
            computer_paddle.write_score()
        elif ball.xcor() < -380:
            player_paddle.score += 1
            player_paddle.write_score()
        ball.reset()

screen.exitonclick()
