from turtle import Turtle

MID_POS = (0, 0)
MID_MID = (0, -20)
MID_LOW = (0, -40)

class Score(Turtle):

    def __init__(self):
        super().__init__()
        self.score = 0
        self.path = ".\\data.txt"
        with open(self.path) as reader:
            self.high_score = int(reader.read())
        self.color("white")
        self.hideturtle()
        self.penup()
        self.font = ('Arial', 12 ,'normal')
        self.font_bold = ('Arial', 12 ,'bold')
        self.reset_pos()


    def update_score(self):
        self.clear()
        self.write(f"Score: {self.score}  |  High Score: {self.high_score}", align='center', font = self.font)

    def reset(self):
        self.setposition(MID_POS)
        if self.high_score < self.score:
            with open(self.path, 'w') as writer:
                writer.write(str(self.score))
                self.high_score = self.score
            self.write(f"Congratulations!", align='center', font = self.font_bold)
            self.setposition(MID_MID)
            self.write(f"You've made a New Highscore: {self.score}.", align='center', font = self.font_bold)
            self.setposition(MID_LOW)
            self.write(f"To play again Press 'P' to Quit press 'Q'", align='center', font = self.font_bold)
        else:
            self.write(f"Game Over!", align='center', font = self.font_bold)
            self.setposition(MID_MID)
            self.write(f"Your Score: {self.score}", align='center', font = self.font_bold)
            self.setposition(MID_LOW)
            self.write(f"To play again Press 'P' to Quit press 'Q'", align='center', font = self.font_bold)
        self.score = 0

    def increment_score(self):
        self.score += 1
        self.update_score()

    def reset_pos(self):
        self.clear()
        self.setposition(2, 280)
        self.update_score()
