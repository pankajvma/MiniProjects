from turtle import Turtle, Screen
import random

tuntun = Turtle()
tuntun.pensize(10)
tuntun.speed("fast")

turtle_colors = ["dark slate blue", "indigo", "dark violet", "dark magenta", "medium violet red", "maroon", 
                    "saddle brown", "dark green", "blue", "orange", "gold", "yellow", "olive drab", "red",
                    "slate gray", "gainsboro", "thistle", "dark goldenrod", "cyan", "navajo white", "dark olive green"]

screen = Screen()

turning_angle = [0, 90, 180, 270]

for _ in range(200):
    tuntun.pencolor(random.choice(turtle_colors))
    tuntun.forward(20)
    tuntun.setheading(random.choice(turning_angle))

screen.exitonclick()
