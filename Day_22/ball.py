from turtle import Turtle

class Ball(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.shape("circle")
        self.color("white")
        self.pu()
        self.y_move =  10
        self.x_move = 10
        self.gear = 0.1

    def move(self):
        new_x = self.xcor() +  self.x_move
        new_y = self.ycor() + self.y_move
        self.goto(new_x, new_y)

    def bounce(self):
        self.y_move *= -1

    def contact(self):
        self.x_move *= -1
        self.gear *= 0.9

    def reset_position(self):
        self.goto(0, 0)
        self.gear = 0.1
        self.contact()

