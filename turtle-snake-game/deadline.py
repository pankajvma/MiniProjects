from turtle import Turtle, Screen
import random


class Deadline(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.penup()
        self.color("red")
        self.speed("fastest")
        self.setposition(-298, 280)
        self.pendown()
        for _ in range(2):
            self.forward(589)
            self.right(90)
            self.forward(570)
            self.right(90)