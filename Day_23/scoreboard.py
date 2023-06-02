from turtle import Turtle

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()

        self.pu()
        self.hideturtle()
        self.level = 1
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-240, 270)
        self.write(f"Level: {self.level}", align="center",font=("Courier",20,"normal"))

    def game_over(self):
        self.goto(0, 0)
        self.write(arg=f"GAME OVER", align="center", font=("Courier",20,"normal"))