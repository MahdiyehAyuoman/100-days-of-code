from turtle import Turtle, Screen
screen = Screen()
starting_positions = [(0, 0), (-20, 0), (-40, 0)]
move_forward_distance = 20

UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    def __init__(self):
        # We'll make these attributes of the class
        self.segments = []
        # Now we'll call a method to create the snake's body
        self.create_snake()

    def create_snake(self):
        # This is a method that handles the segment creation
        for position in starting_positions:
             self.add_segment(position)

    def add_segment(self, position):
        new_segment = Turtle("square")
        new_segment.penup()
        new_segment.color("white")
        new_segment.goto(position)
        self.segments.append(new_segment)


    def extend(self):
        # Add a new segment to the snake
        self.add_segment(self.segments[-1].position())

    def move_snake(self):
        for seg_num in range(len(self.segments)-1, 0, -1):
            new_x = self.segments[seg_num - 1].xcor()
            new_y = self.segments[seg_num - 1].ycor()
            self.segments[seg_num].goto(new_x, new_y)
        self.segments[0].forward(move_forward_distance)

    def turn_up(self):
        if self.segments[0].heading() != DOWN:
            self.segments[0].setheading(UP)

    def turn_down(self):
        if self.segments[0].heading() != UP:
            self.segments[0].setheading(DOWN)

    def turn_left(self):
        if self.segments[0]  != RIGHT:
            self.segments[0].setheading(LEFT)

    def turn_right(self):
        if self.segments[0].heading() != LEFT:
            self.segments[0].setheading(RIGHT)
