from turtle import Turtle, Screen
import time


class Paddle(Turtle):

    def __init__(self, x_position, color):
        super().__init__()
        self.color(color)
        self.penup()
        self.setposition(x_position, 0)
        self.shape('square')
        self.shapesize(5, 1)

    def go_up(self):
        new_y_cor = self.ycor() + 40
        self.sety(new_y_cor)

    def go_down(self):
        new_y_cor = self.ycor() - 40
        self.sety(new_y_cor)
