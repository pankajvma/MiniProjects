from turtle import Turtle

FONT = ("Courier", 24, "normal")


class Levelboard(Turtle):
    def __init__(self):
        super().__init__()
        self.color("black")
        self.penup()
        self.hideturtle()
        self.level = 0
        self.font = FONT
        self.update_levelboard()

    def update_levelboard(self):
        self.clear()
        self.goto(-290, 266)
        self.write(f"Lavel: {self.level}", align="left", font = self.font)


    def level_up(self):
        self.level += 1
        self.update_levelboard()



    def game_over(self):
        self.setposition(0, 0)
        self.color('black')
        self.write(f"Game Over! At level: {self.level}", align='center', font = ("Courier", 20, "bold"))

