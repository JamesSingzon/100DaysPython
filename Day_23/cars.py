from turtle import Screen, Turtle
from random import choice, randint

X_START = 300

class Cars(Turtle):
    def __init__(self) -> None:
        super().__init__(shape="square")

        colors = ["orange", "red", "yellow","blue", "green", "purple"]
        self.pu()
        self.color(choice(colors))
        self.shapesize(stretch_len=2, stretch_wid=1)
        self.goto(X_START, randint(-240, 250))

    def car_crawl(self):
        self.backward(10)