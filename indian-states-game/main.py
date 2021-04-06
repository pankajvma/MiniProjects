from turtle import Turtle, Screen
import turtle as turtle
import map_data as map
import time

writer = Turtle()
writer.hideturtle()
writer.penup()
writer.speed("fastest")
writer.color('green')

screen = Screen()
screen.screensize(600,600)
FONT_STYLE = ('Arial',8,'normal')
FINAL_FONT_STYLE = ('Arial',18,'bold')

screen.title("Guess all the Indian states and Union Territories")

indian_map = "india.gif"

screen.addshape(indian_map)

india = Turtle()
india.shape(indian_map)

def exit_from_game(total_correct_answers):
    for state in map.states:
        writer.goto(map.map_dict[state])
        writer.write(state, align = "center", font = FONT_STYLE)
    time.sleep(5)
    india.clear()
    india.hideturtle()
    screen.bgcolor('green')
    writer.color("white")
    writer.goto(0, 0)
    writer.write(f"You guessed {total_correct_answers} states correctly.", align = "center", font = FINAL_FONT_STYLE)
    time.sleep(5)
    exit()

    

def start_game():
    is_on = True
    count = 0
    while is_on:
        answer_state = screen.textinput(title = "Guess the State", prompt = "Enter the missing states. \nEnter 'Q' to quit.").split(" ")
        answer = ''
        for word in answer_state:
            if word.title() != "And":
                answer += word.title()
            else:
                answer += ' and '
        if answer != 'Q':
            if answer in map.map_dict:
                count += 1
                writer.goto(map.map_dict[answer])
                writer.write(answer.title(), align = "center", font = FONT_STYLE)
                time.sleep(1)
        else:
            is_on = False
    
    exit_from_game(count)

start_game()

  
turtle.mainloop()


# Getting coordinnates of states from graph

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
