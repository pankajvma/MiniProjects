from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
import random
from score_board import Score
from deadline import Deadline

screen = Screen()
score = Score()

screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake and Food")
screen.tracer(0)

screen.listen()

deadline = Deadline()
snake = Snake()
food = Food()


def start_game():
    is_on = True

    while is_on:
        screen.update()
        time.sleep(0.08)

        snake.move()

        if snake.head.distance(food) <= 15:
            food.refresh()
            snake.extend()
            score.increment_score()

        
        if snake.head.xcor() > 290 or snake.head.xcor() < -300 or snake.head.ycor() > 280 or snake.head.ycor() < -300:
            is_on =False


        for segment in snake.segments[1:]:
            if snake.head.distance(segment) <= 10:
                is_on =False
                break

    score.reset()



def restart_game():
    score.reset_pos()
    snake.reset()
    start_game()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
screen.onkey(restart_game, "p")
screen.onkey(exit, "q") 


start_game()

screen.exitonclick()

