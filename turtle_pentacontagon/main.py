from turtle import Turtle, Screen
import random

tim = Turtle()
screen = Screen()

screen.colormode(255)

number_of_sides = 3
screen.setup(1000, 800)

tim.speed("fastest")
tim.penup()
tim.setposition(0, 380)
tim.pendown()


while number_of_sides <= 50:
    angle = 360 / number_of_sides
    r = random.randint(10, 255)
    g = random.randint(10, 255)
    b = random.randint(10, 255)
    tup = (r, g, b)
    tim.pencolor(tup)
    for _ in range(number_of_sides):
        tim.forward(40)
        tim.right(angle)
    number_of_sides += 1

screen.exitonclick()