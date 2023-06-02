from turtle import Screen, Turtle
import time
from paddle import Paddle
from ball import Ball
from scoreboard import Scoreboard

#Create the screen.
screen = Screen()
screen.setup(width=800, height=600)
screen.bgcolor("black")
screen.title("Pong")
screen.listen()
screen.tracer(0)

net = Turtle(shape="square")
net.color("white")
net.speed("fastest")
net.pu()
net.goto(0,580)
net.setheading(270)
while net.ycor() > -580:
    net.pd()
    net.forward(20)
    net.pu()
    net.forward(20)

#Create and move a paddle.
#Create another paddle.

r_paddle = Paddle((350, 0))
l_paddle = Paddle((-350, 0))
scoreboard = Scoreboard()

screen.onkey(fun=r_paddle.paddle_up, key="Up")
screen.onkey(fun=r_paddle.paddle_down, key="Down")
screen.onkey(fun=l_paddle.paddle_up, key="w")
screen.onkey(fun=l_paddle.paddle_down, key="s")

#Create the ball and make it move.
ball = Ball()

game_on = True
while game_on:
    time.sleep(ball.gear)
    screen.update()
    ball.move()

#Detect colision with wall and bounce.
    if ball.ycor() > 280 or ball.ycor() < -280:
        ball.bounce()
#Detect colision with paddle.
    if ball.distance(r_paddle) < 70 and ball.xcor() < 320 or ball.distance(l_paddle) < 70 and ball.xcor() > -320:
        ball.contact()
#Detect when right paddle misses.
    if ball.xcor() > 380: 
        ball.reset_position()
        scoreboard.l_point()
        scoreboard.update_scoreboard()

    if ball.xcor() < -380:
        ball.reset_position()
        scoreboard.r_point()
        scoreboard.update_scoreboard()
#Keep score.





#Create another paddle.
#Create the ball and make it move.
#Detect colision with wall and bounce.
#Detect colision with paddle.
#Detect when paddle misses.
#Keep score.


screen.exitonclick()