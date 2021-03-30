from turtle import Turtle, Screen
import time


class Ball(Turtle):

    def __init__(self):
        super().__init__()
        self.shape('circle')
        self.penup()
        self.color('white')
        self.x_move = .7
        self.y_move = .7

    def move(self):
        new_x_cor = self.xcor() + self.x_move
        new_y_cor = self.ycor() + self.y_move  #The sign of y_move will change everytime it bounces
        self.goto(new_x_cor, new_y_cor)


    def bounce_y(self):
        self.y_move *= -1

    def bounce_x(self):
        self.x_move *= -1

    def reset(self):
        self.goto(0, 0)
        self.x_move = .7
        self.y_move = .7

    