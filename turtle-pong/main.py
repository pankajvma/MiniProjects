from turtle import Turtle, Screen
import time
from paddle import  Paddle
from ball import Ball
from score_board import Score
from seperator import Seperator

screen = Screen()
screen.bgcolor("green")
screen.setup(800, 600)
screen.title("Pong")
screen.tracer(0)
WINNING_POINNTS = 10

right_paddle = Paddle(380, "blue")
left_paddle = Paddle(-390, "red")


draw_line = Seperator()


ball = Ball()
score = Score()

screen.listen()

screen.onkey(right_paddle.go_up, "Up")
screen.onkey(right_paddle.go_down, "Down")
screen.onkey(left_paddle.go_up, "w")
screen.onkey(left_paddle.go_down, "s")

print(ball.shapesize())


is_on = True

while is_on:
    ball.move()
    screen.update()

    if abs(ball.ycor()) > 290:
        ball.bounce_y()

    if ball.distance(right_paddle) < 50 and ball.xcor() > 355 or ball.distance(left_paddle) < 50 and ball.xcor() < -365:
        ball.x_move += .05
        ball.y_move += .05
        ball.bounce_x()


    if ball.xcor() > 390:
        score.left_point()
        time.sleep(1)
        ball.reset()

    if ball.xcor() < -390:
        score.right_point()
        time.sleep(1)
        ball.reset()

    if score.left_score == WINNING_POINNTS or score.right_score == WINNING_POINNTS:
        is_on = False

score.game_over()
screen.exitonclick()