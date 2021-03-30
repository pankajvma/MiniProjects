from turtle import Turtle


class Seperator(Turtle):

    def __init__(self):
        super().__init__()
        self.hideturtle()
        self.color('white')
        self.width(2)
        self.penup()
        self.goto(0, 300)
        self.setheading(270)
        self.pensize()
        self.pendown()
        self.draw()


    def draw(self):
        for _ in range(20):
            self.penup()
            self.forward(15)
            self.pendown()
            self.forward(15)