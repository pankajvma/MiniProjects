from turtle import Turtle, Screen
import time

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0) ]
UP = 90
LEFT = 180
RIGHT = 0
DOWN = 270

class Snake:

    def __init__(self):
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]


    def create_snake(self):
        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        self.new_turtle = Turtle("square")
        self.new_turtle.color("white")
        self.new_turtle.penup()
        self.new_turtle.speed("slow")
        self.new_turtle.setposition(position)
        self.segments.append(self.new_turtle)

    def extend(self):
        self.add_segment(self.segments[-1].position())

    def move(self):
        for segment_number  in range(len(self.segments)-1, 0, -1):
            temp_x = self.segments[segment_number - 1].xcor()
            temp_y = self.segments[segment_number - 1].ycor()

            self.segments[segment_number].goto(temp_x, temp_y)

        self.segments[0].forward(20)


    def up(self):
        if self.head.heading() != DOWN:
            self.head.setheading(UP)

    def left(self):
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)

    def right(self):
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)

    def down(self):
        if self.head.heading() != UP:
            self.head.setheading(DOWN)


    def reset(self):
        for segment in self.segments:
            segment.hideturtle()
        self.segments.clear()
        self.create_snake()
        self.head = self.segments[0]
