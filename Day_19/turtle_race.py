from turtle import Turtle, Screen, colormode
from random import randint, choice

screen = Screen()
screen.setup(width = 500, height = 400)
user_bet = screen.textinput(title = "Make your bet", prompt = "Which turtle will win the race?  Enter a color: ")
colors = ["red", "orange", "yellow", "green", "blue", "purple"]
all_turtles = []

is_race_on = False
if user_bet:
    is_race_on = True





y_start = -100
for turtle_index in range(0,6):

    new_turtle = Turtle(shape = "turtle")
    new_turtle.color(colors[turtle_index])
    new_turtle.pu()
    new_turtle.goto(-240,y_start)
    all_turtles.append(new_turtle)
    y_start += 40


while is_race_on:
    rand_distance = randint(0, 10)
    choice(all_turtles).forward(rand_distance)
    for finisher in all_turtles:
        if finisher.xcor() >= 250:
            winning_color = finisher.pencolor()
            is_race_on = False
if winning_color.lower() == user_bet.lower():
    print(f"You've won!  Stunning performance by the {winning_color} turtle!")
else:
    print(f"You've lost!  Stunning performance by the {winning_color} turtle!")



screen.exitonclick()