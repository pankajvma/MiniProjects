from turtle import Turtle, Screen
import time
from snake import Snake
from food import Food
import random
from score_board import Score
from top_deadline import Deadline

screen = Screen()
score = Score()

screen.bgcolor("black")
screen.setup(600, 600)
screen.title("Snake and Food")
screen.tracer(0)


screen.update()
screen.listen()

deadline = Deadline()
snake = Snake()
food = Food()

screen.onkey(snake.up, "Up")
screen.onkey(snake.down, "Down")
screen.onkey(snake.left, "Left")
screen.onkey(snake.right, "Right")
 

while True:
    screen.update()
    time.sleep(0.1)

    snake.move()

    if snake.head.distance(food) <= 15:
        food.refresh()
        score.update_score()

    
    if snake.head.xcor() > 280 or snake.head.xcor() < -280 or snake.head.ycor() > 280 or snake.head.ycor() < -280:
        break

score.game_over()
screen.exitonclick()