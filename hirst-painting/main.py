import colorgram
from turtle import Turtle, Screen
import random
import turtle as t

colors = colorgram.extract('C:\\Users\\Lenovo\\Documents\\Git Repos\\MiniProjects\\hirst-painting\\img.jpg', 30)

extracted_colors = []

for color in colors:
    r = color.rgb.r  #extracting r from RGB(r, g, b)
    g = color.rgb.g  #extracting g from RGB(r, g, b)
    b = color.rgb.b  #extracting b from RGB(r, g, b)

    extracted_colors.append((r, g, b))

tuntun = Turtle()
tuntun.hideturtle()
screen = Screen()
t.colormode(255)
tuntun.penup()
tuntun.speed("fastest")
tuntun.setposition(-300, -200)


for count in range(1, 101):
    tuntun.dot(20, random.choice(extracted_colors))
    tuntun.forward(50)
    if count % 10 == 0:
        tuntun.left(90)
        tuntun.forward(50)
        tuntun.left(90)
        tuntun.forward(500)
        tuntun.left(180)

# Second method

# last_tuned_left = False

# def draw_from_left():
#     tuntun.left(90)
#     tuntun.fd(50)
#     tuntun.left(90)

# def draw_from_right():
#     tuntun.right(90)
#     tuntun.fd(50)
#     tuntun.right(90)

# for _ in range(10):
#     for _ in range(10):
#         tuntun.dot(20, random.choice(extracted_colors))
#         tuntun.forward(50)
#     tuntun.dot(20, random.choice(extracted_colors))
#     if not last_tuned_left:
#         draw_from_left()
#         last_tuned_left = True
#     else:
#         draw_from_right()
#         last_tuned_left = False
        
screen.exitonclick()