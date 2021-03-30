from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.color("white")
        self.penup()
        self.hideturtle()
        self.left_score = 0
        self.right_score = 0
        self.font = ("Courier", 80, "normal")
        self.update_scoreboard()

    def update_scoreboard(self):
        self.clear()
        self.goto(-100, 200)
        self.write(self.left_score, align="center", font = self.font)
        self.goto(100, 200)
        self.write(self.right_score, align="center", font = self.font)

    def left_point(self):
        self.left_score += 1
        self.update_scoreboard()

    def right_point(self):
        self.right_score += 1
        self.update_scoreboard()


    def game_over(self):
        self.setposition(0, 0)
        self.color('black')
        self.write(f"Game Over!\nLeft's Score: {self.left_score}\nRight's Scrpre:{self.right_score}", align='center', font = ("Courier", 20, "normal"))
