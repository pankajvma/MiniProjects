from turtle import Turtle
import random

turtle_colors = turtle_colors = ["dark slate blue", "indigo", "dark violet", "dark magenta", "medium violet red", "maroon", 
                    "saddle brown", "dark green", "blue", "orange", "gold", "yellow", "olive drab", "red",
                    "slate gray", "gainsboro", "thistle", "dark goldenrod", "cyan", "navajo white", "dark olive green"]

class RandomTurle:
    def __init__(self):
        self.timmy = Turtle()
        self.timmy.speed('fastest')
        self.timmy.shape("turtle")
        self.timmy.penup()
        x = random.randint(-300, 300)
        y =random.randint(-300, 300)
        self.timmy.setpos(x, y)
        self.timmy.pendown()
        self.timmy.color(random.choice(turtle_colors))



