from turtle import Turtle, Screen

tim = Turtle()
screen = Screen()


def move_forward():
    tim.forward(10)
def move_backward():
    tim.backward(10)
def turn_clockwise():
    tim.setheading(tim.heading() - 10)
def turn_counterclockwise():
    tim.setheading(tim.heading() + 10)
def clear_drawing():
    tim.clear()

screen.listen()
screen.onkey(key = "w", fun = move_forward)
screen.onkey(key = "s", fun = move_backward)
screen.onkey(key = "a", fun = turn_counterclockwise)
screen.onkey(key = "d", fun = turn_clockwise)
screen.onkey(key = "c", fun = clear_drawing)

screen.exitonclick()