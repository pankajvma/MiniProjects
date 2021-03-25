from turtle import Turtle, Screen
import random


def color_turtles():
    tuntun.color("red")
    tintun.color("orange")
    tintin.color("yellow")
    tuntin.color("green")
    tunton.color("blue")
    tontin.color("indigo")
    tinton.color("violet")

def set_turtles():
    y = -100
    for tortoise in turtles:
        tortoise.setposition(-250, y)
        y += 40


def draw_finish_line():
    line.setposition(230, -140)
    line.left(90)
    line.pendown()
    line.forward(300)


tuntun = Turtle()
tintun = Turtle()
tintin = Turtle()
tuntin = Turtle()
tunton = Turtle()
tontin = Turtle()
tinton = Turtle()

line = Turtle()
line.hideturtle()
line.pencolor("black")
line.penup()
line.pensize(2)

turtles = [tuntun, tintun, tintin, tuntin, tunton, tontin, tinton]

for tortoise in turtles:
    tortoise.shape("turtle")
    tortoise.penup()

screen = Screen()
screen.setup(width = 550, height = 400)
choice=screen.textinput("Choose your turtle", "Choose from violet, indigo, blue, green, yellow, orange, red  (VIBGYOR):").lower()

color_turtles()


set_turtles()


draw_finish_line()


def start_race():
    winner = ""
    while True:
        runner = random.choice(turtles)
        runner.forward(5)
        if runner.xcor() == 230:
            winner += runner.color()[0]
            break
    return winner

winner = start_race()

if winner == choice:
    print(f"Congratulations! Your {choice.title()} turtle is the winner")
else:
    print(f"Your {choice.title()} turtle couldn't make it to the finish line first.\n{winner.title()} turtle is the winner")


screen.exitonclick()

