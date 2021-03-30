from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.setposition(2, 280)
        self.font = ('Arial', 12 ,'normal')
        self.write(f"Score: {self.score}", align='center', font = self.font)


    def update_score(self):
        self.score += 1
        self.clear()
        self.write(f"Score: {self.score}", align='center', font = self.font)
