import turtle
STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0


class Snake:
    def __init__(self) -> None:
        self.xcor = 0
        self.snake_segments = []
        self.create_snake()

    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)
            # self.snake = turtle.Turtle()
            # self.snake.color("white")
            # self.snake.shape("square")
            # self.snake.pu()
            # self.snake.setx(self.xcor*-20)
            # self.xcor+= 1
            # self.snake_segments.append(self.snake)

    def add_segment(self, position):
        self.snake = turtle.Turtle()
        self.snake.color("white")
        self.snake.shape("square")
        self.snake.pu()
        self.snake.goto(position)
        self.snake_segments.append(self.snake)

    def extend(self):
        self.add_segment(self.snake_segments[-1].position())

    def reset(self):
        for seg in self.snake_segments:
            seg.goto(1000, 1000)
        self.snake_segments.clear()
        self.create_snake()


    def move(self):
        for seg_num in range(len(self.snake_segments)-1, 0, -1):
            new_x = self.snake_segments[seg_num - 1].xcor()
            new_y = self.snake_segments[seg_num - 1].ycor()
            self.snake_segments[seg_num].goto(new_x, new_y)
        self.snake_segments[0].forward(MOVE_DISTANCE)

    def up(self):
        if self.snake_segments[0].heading() != DOWN:
            self.snake_segments[0].setheading(UP)

    def down(self):
        if self.snake_segments[0].heading() != UP:
            self.snake_segments[0].setheading(DOWN)

    def left(self):
        if self.snake_segments[0].heading() != RIGHT:
            self.snake_segments[0].setheading(LEFT)

    def right(self):
        if self.snake_segments[0].heading() != LEFT:
            self.snake_segments[0].setheading(RIGHT)