from turtle import Turtle, Screen
import random
import turtle as t

tuntun = Turtle()
tuntun.speed("fastest")
tuntun.pensize(2)

t.colormode(255)

def get_random_color():
    r = random.randint(1, 255)
    g = random.randint(1, 255)
    b = random.randint(1, 255)
    tup = (r, g, b)         # creating tuple to change colormode
    return tup

screen = Screen()

angle = 0

while angle <= 360:
    random_color = get_random_color()
    tuntun.color(random_color)
    tuntun.circle(125)
    angle += 5
    tuntun.setheading(angle)
    tuntun.fd(5)        # to create a little circle at center

screen.exitonclick()
