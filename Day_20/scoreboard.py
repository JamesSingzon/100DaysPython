from turtle import Turtle
ALIGNMENT = "center"
FONT = ("Courier", 16, "normal")

class Scoreboard(Turtle):
    def __init__(self) -> None:
        super().__init__()
        self.color("white")
        self.hideturtle()
        self.pu()
        self.score = 0
        with open("/Users/jamessingzon/Desktop/100DaysPython/Day_20/data.txt") as file:
            self.high_score = int(file.read())
        self.goto(0,280)
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.write(arg=f"Score: {self.score} High Score: {self.high_score}", align=ALIGNMENT, font=FONT)

    # def game_over(self):
    #     self.goto(0, 0)
    #     self.write(arg=f"GAME OVER", align=ALIGNMENT, font=FONT)

    def reset(self):
        if self.score > self.high_score:
            self.high_score = self.score
            with open("/Users/jamessingzon/Desktop/100DaysPython/Day_20/data.txt", mode="w") as file:
                file.write(f"{self.high_score}")
            self.score = 0
            self.update_scoreboard()



    def increase_score(self):
        self.score += 1
        self.clear()
        self.update_scoreboard()


