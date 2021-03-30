from turtle import Turtle, Screen
import random


class Deadline(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.setposition(-300, 280)
        self.pendown()
        self.forward(600)