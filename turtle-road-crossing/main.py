import time
from turtle import Screen
from player import Player
from car_manager import CarManager
from scoreboard import Levelboard

screen = Screen()
screen.title("Roadd Crossing")
screen.setup(width=600, height=600)
screen.tracer(0)

player = Player()
level_board = Levelboard()

screen.listen()
screen.onkey(player.move_up, "Up")

car = CarManager()

game_is_on = True
while game_is_on:
    time.sleep(0.1)
    screen.update()
    car.create_car()
    car.drive()

    for cr in car.cars:
        if cr.distance(player) < 20:
            screen.update()
            game_is_on = False

    if player.is_at_finish_line():
        time.sleep(1)
        level_board.level_up()
        car.reset()
        player.reset()


level_board.game_over()
screen.exitonclick()