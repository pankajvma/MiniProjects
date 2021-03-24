from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)
screen.setup(1000, 800)

tim.speed("fastest")
tim.penup()
tim.setposition(0, 380)
tim.pendown()


def draw_shape(number_of_sides, angle, tup):
    tim.pencolor(tup)
    for _ in range(i):
        tim.forward(40)
        tim.right(angle)

for i in range(3, 51):
    angle = 360 / i
    r = random.randint(10, 255)
    g = random.randint(10, 255)
    b = random.randint(10, 255)
    tup = (r, g, b)
    draw_shape(i, angle, tup)

screen.exitonclick()