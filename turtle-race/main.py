from turtle import Turtle, Screen
import random

colors = ["red", "orange", "yellow", "green", "blue", "indigo", "violet"]

def draw_finish_line():
    line = Turtle()
    line.hideturtle()
    line.pencolor("black")
    line.penup()
    line.pensize(2)
    line.setposition(230, -140)
    line.left(90)
    line.pendown()
    line.forward(300)


turtles = []

def set_turtles():
    y = -100
    for i in range(7):
        tuntun = Turtle()
        tuntun.shape("turtle")
        tuntun.penup()
        tuntun.color(colors[i])
        tuntun.setposition(-250, y)
        y += 40
        turtles.append(tuntun)


def start_race():
    winner = ""
    while True:
        runner = random.choice(turtles)
        runner.forward(5)
        if runner.xcor() == 230:
            winner += runner.color()[0]
            break
    if winner == choice:
        print(f"Congratulations! Your {choice.title()} turtle is the winner")
    else:
        print(f"Your {choice.title()} turtle couldn't make it to the finish line first.\n{winner.title()} turtle is the winner")

screen = Screen()
screen.setup(width = 550, height = 400)
choice=screen.textinput("Choose your turtle", "Choose from violet, indigo, blue, green, yellow, orange, red  (VIBGYOR):").lower()

set_turtles()

draw_finish_line()

start_race()

screen.exitonclick()