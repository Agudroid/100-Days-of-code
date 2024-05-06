from turtle import Turtle

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    snake_length = 3
    snake_segments = []
    snake_head = None

    def __init__(self):
        x_cord = 0
        for i in range(0, self.snake_length):
            new_segment = Turtle()
            new_segment.penup()
            new_segment.color("White")
            new_segment.pencolor("White")
            new_segment.speed('fastest')

            if i == 0:
                new_segment.shape("arrow")
            new_segment.shape('square')
            new_segment.goto(x_cord, 0)
            self.snake_segments.append(new_segment)
            x_cord -= 20
        self.snake_head = self.snake_segments[0]

    def __move__(self, action):
        new_x, new_y = 0, 0
        for segment in self.snake_segments:
            if self.snake_segments.index(segment) == 0:
                new_x = segment.xcor()
                new_y = segment.ycor()

                if action == "Up" and self.snake_head.heading() != DOWN:
                    segment.setheading(90)

                elif action == "Down" and self.snake_head.heading() != UP:
                    segment.setheading(270)

                elif action == "Right" and self.snake_head.heading() != LEFT:
                    segment.setheading(0)

                elif action == "Left" and self.snake_head.heading() != RIGHT:
                    segment.setheading(180)

                segment.forward(20)
            else:
                old_x = segment.xcor()
                old_y = segment.ycor()
                segment.goto(new_x, new_y)
                new_x = old_x
                new_y = old_y

    def grow_snake(self):
        new_segment = Turtle()
        new_segment.penup()
        new_segment.color("White")
        new_segment.pencolor("White")
        new_segment.shape('square')
        new_segment.goto(self.snake_segments[-1].xcor(), self.snake_segments[-1].ycor())
        self.snake_segments.append(new_segment)

    def up(self):
        self.__move__("Up")

    def down(self):
        self.__move__("Down")

    def left(self):
        self.__move__("Left")

    def right(self):
        self.__move__("Right")

    def continue_move(self):
        self.__move__("")

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.__init__()