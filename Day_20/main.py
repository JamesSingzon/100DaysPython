from turtle import Screen
from snake import Snake
from food import Food
from scoreboard import Scoreboard
import time


screen = Screen()
screen.setup(width=600, height=600)
screen.bgcolor("black")
screen.title("My Snake Game")
screen.tracer(0)


# Create a snake body.

snake = Snake()
food = Food()
scoreboard = Scoreboard()

# Control the snake.

screen.listen()
screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")


# Move the snake.
game_on = True
while game_on:
    screen.update()
    time.sleep(0.1)
    snake.move()

# Detect colision with food.
# Create a scoreboard.

    if snake.snake_segments[0].distance(food) < 15:
        print("nom nom nom")
        food.refresh()
        scoreboard.increase_score()
        snake.extend()

# Detect a colision with wall. (Game end)
    if snake.snake_segments[0].xcor() > 280 or snake.snake_segments[0].xcor() < -280 or snake.snake_segments[0].ycor() > 280 or snake.snake_segments[0].ycor() < -280:
        scoreboard.reset()
        snake.reset()

# Detect a colision with tail. (Game end)
    for segment in snake.snake_segments[1:]:
        if snake.snake_segments[0].distance(segment) < 10:
           scoreboard.reset()
           snake.reset()


screen.exitonclick()

