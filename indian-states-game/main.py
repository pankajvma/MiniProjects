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
FINAL_FONT_STYLE = ('Arial',13,'bold')

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
    writer.goto(0, -20)
    writer.write("Please check the states_to_remember.csv file to find out which states you missed.", align = "center", font = FINAL_FONT_STYLE)
    time.sleep(5)
    exit()
    

def start_game():
    is_on = True
    right_guesses = []
    missed_states = []
    all_states = map.states.to_list()
    while is_on and len(right_guesses) <= 36:
        answer_state = screen.textinput(title = f"{len(right_guesses)}/36 states", prompt = "Enter the missing states. \nEnter 'Q' to quit.").split(" ")
        answer = ''
        for word in answer_state:
            if word.title() == "And":
                answer += ' and '
            elif word.title() == "Nicobar" or word.title() == "Nagar":
                answer += word.title()+' '
            else:
                answer += word.title()
        if answer != 'Q':
            if answer in map.map_dict:
                right_guesses.append(answer)
                writer.goto(map.map_dict[answer])
                writer.write(answer.title(), align = "center", font = FONT_STYLE)
                time.sleep(1)
        else:
            is_on = False
            for state in right_guesses:
                if state not in all_states:
                    missed_states.append(state)
            map.save(missed_states)   
    
    exit_from_game(len(right_guesses))

start_game()

  
turtle.mainloop()


# Getting coordinnates of states from graph

# def get_mouse_click_coor(x, y):
#     print(x, y)

# turtle.onscreenclick(get_mouse_click_coor)
