from turtle import Turtle, Screen

timmy = Turtle()
screen = Screen()
timmy.shape("arrow")
timmy.color("black")
#
# for i in range(5):
#     timmy.begin_fill()
#     for j in range(4):
#         timmy.left(90)
#         timmy.forward(10)
#     timmy.forward(20)
#     timmy.end_fill()

i = 0
is_painting = True
while i < 10:
    timmy.pendown() if is_painting else timmy.penup()
    timmy.forward(10)
    is_painting = not is_painting
    i += 1
# for i in range(10):
#     timmy.forward(10)
#     timmy.penup()
#     timmy.forward(10)
#     timmy.pendown()
screen.exitonclick()
