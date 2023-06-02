from turtle import Screen, Turtle
import time
from scoreboard import Scoreboard
from frogger import Frogger
from cars import Cars

traffic = []
count = 0

screen = Screen()
screen.setup(width=600, height=600)
screen.listen()
screen.tracer(0)
screen.title("Frogger")


frogger = Frogger()
level = Scoreboard()

screen.onkey(fun=frogger.move_forward, key="Up")
screen.onkey(fun=frogger.move_backward, key="Down")


game_on = True
while game_on:
    level.update_scoreboard()
    time.sleep(0.1)
    screen.update()

    if count % 6 == 0:
        traffic.append(Cars())
    for car in traffic:
        car.car_crawl()


    if frogger.ycor() > 270:
        level.level += 1
        level.update_scoreboard()
        frogger.reset_position()

    for car in traffic:
        if frogger.distance(car) < 20:
            game_on = False
            level.game_over()
    count += 1
screen.exitonclick()