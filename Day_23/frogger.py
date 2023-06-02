from turtle import Turtle

class Frogger(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.color("green")
        self.setheading(90)
        self.shapesize(stretch_len=2, stretch_wid=2)
        self.pu()
        self.reset_position()

    def move_forward(self):
        self.forward(20)

    def move_backward(self):
        self.backward(20)

    def reset_position(self):
        self.goto(0, -260)
