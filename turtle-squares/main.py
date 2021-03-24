from squares import RandomTurle
from turtle import Screen
import random


turtles = []

for _ in range(50):
    tim = RandomTurle()
    turtles.append(tim)

screen = Screen()

for tortoise in turtles:
    step_length = random.randint(10, 100)
    for _ in range(4):
        tortoise.timmy.forward(step_length)
        tortoise.timmy.right(90)

screen.exitonclick()