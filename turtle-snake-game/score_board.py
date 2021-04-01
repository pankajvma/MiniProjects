from turtle import Turtle

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.high_score = 0
        self.color("white")
        self.hideturtle()
        self.penup()
        self.font = ('Arial', 12 ,'normal')
        self.reset_pos()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align='center', font = self.font)

    def reset(self):
        self.setposition(0, 0)
        if self.high_score < self.score:
            self.high_score = self.score
            self.write(f"Congratulations!\nYou've made a New Highscore: {self.score}.\n To play again Press 'P' to Quit press 'Q'", align='center', font = self.font)
        else:
            self.write(f"Game Over!\nYour Score: {self.score}\n To play again Press 'P' to Quit press 'Q'", align='center', font = self.font)
        self.score = 0

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset_pos(self):
        self.clear()
        self.setposition(2, 280)
        self.update_score()
