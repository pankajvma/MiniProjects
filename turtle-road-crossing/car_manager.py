from turtle import Turtle
import random

COLORS = ["red", "orange", "yellow", "green", "blue", "purple"]
STARTING_MOVE_DISTANCE = 5
MOVE_INCREMENT = 10


class CarManager:

    def __init__(self):
        self.cars = []
        

    def create_car(self):
        random_chance = random.randint(1, 6)
        if random_chance == 6:
            car = Turtle()
            car.shape("square")
            car.shapesize(1, 2)
            car.penup()
            car.color(random.choice(COLORS))
            x = random.randint(320, 360)
            y = random.randint(-250, 250)
            car.setposition(320, y)
            car.setheading(180)
            self.cars.append(car)

    def drive(self):
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)

    def reset(self):
        global STARTING_MOVE_DISTANCE 
        STARTING_MOVE_DISTANCE += MOVE_INCREMENT
        for car in self.cars:
            car.forward(STARTING_MOVE_DISTANCE)


    

