from turtle import Turtle, Screen
import random

tuntun = Turtle()
tuntun.pensize(5)
tuntun.speed("fast")
tuntun.penup()
tuntun.setposition(-10, -10)
tuntun.pendown()

screen = Screen()

screen.setup(700, 700)

graph_maker = Turtle()
graph_maker.pensize(1)
graph_maker.speed("fastest")
graph_maker.penup()
graph_maker.setposition(-350, -350)
graph_maker.pendown()


def draw_from(direction):
    graph_maker.forward(700)
    graph_maker.penup()
    if direction == "left":
        graph_maker.left(90)
    else:
        graph_maker.right(90)
    graph_maker.forward(20)
    graph_maker.pendown()
    if direction == "left":
        graph_maker.left(90)
    else:
        graph_maker.right(90)
        

def generate_graph():
    for _ in range(17):
        draw_from("left")
        draw_from("right")

    graph_maker.right(90)

    for _ in range(18):
        draw_from("left")
        draw_from("right")

generate_graph()

turtle_colors = ["dark slate blue", "indigo", "dark violet", "dark magenta", "medium violet red", "maroon", 
                    "saddle brown", "dark green", "blue", "orange", "gold", "yellow", "olive drab", "red",
                    "slate gray", "gainsboro", "thistle", "dark goldenrod", "cyan", "navajo white", "dark olive green"]

turning_angle = [0, 90, 180, 270]


for _ in range(200):
    tuntun.pencolor(random.choice(turtle_colors))
    tuntun.forward(20)
    tuntun.setheading(random.choice(turning_angle))

screen.exitonclick()
