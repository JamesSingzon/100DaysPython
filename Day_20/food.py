from turtle import Turtle
from random import randint

class Food(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.shape("circle")
        self.pu()
        self.shapesize(stretch_len=0.5,stretch_wid=0.5)
        self.speed("fastest")
        self.color("blue")
        self.refresh()

    def refresh(self):
        random_x = randint(-270,270)
        random_y = randint(-270,270)
        self.goto(random_x,random_y)

