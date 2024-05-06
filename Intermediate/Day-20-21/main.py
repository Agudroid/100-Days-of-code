import time
from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard

screen = Screen()
screen.setup(600, 600)
screen.tracer(0)
screen.bgcolor("black")
screen.title("Snake Game")

is_game_on = True

snake = Snake()
food = Food()
scoreboard = Scoreboard()


screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
while is_game_on:
    screen.update()
    time.sleep(0.1)
    snake.continue_move()
    screen.update()

    # Detect food collision
    if snake.snake_head.distance(food) < 20:
        food.refresh()
        snake.grow_snake()
        scoreboard.write_score()
        print("nom nom nom")

    # Detect wall collision
    if (snake.snake_head.xcor() > 280 or snake.snake_head.xcor() < -280 or snake.snake_head.ycor() > 280 or
            snake.snake_head.ycor() < -280):

        is_game_on = False
        scoreboard.game_over()

    # Detect tail collision
    for segment in snake.snake_segments[1:]:

        if snake.snake_head.distance(segment) < 10:
            is_game_on = False
            scoreboard.game_over()

screen.exitonclick()
