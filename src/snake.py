"""
Module for the Snake class used in the Snake game.

Provides functionality to create, move, and grow the snake, 
as well as change its direction.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from turtle import Turtle
from logger import logger

STARTING_POSITIONS = [(0, 0), (-20, 0), (-40, 0)]
MOVE_DISTANCE = 20
UP = 90
DOWN = 270
LEFT = 180
RIGHT = 0

class Snake:
    """
    Represents the snake in the game.

    Attributes:
        turtle_factory (callable): Factory function to create Turtle objects.
        segments (list): List of Turtle objects representing the snake segments.
        head (Turtle): The head segment of the snake.
    """
    def __init__(self, turtle_factory=Turtle):
        """
        Initialize a Snake object with starting segments.

        Args:
            turtle_factory (callable, optional): Factory function to create Turtle objects.
                Defaults to the Turtle class.
        """
        self.turtle_factory = turtle_factory
        self.segments = []
        self.create_snake()
        self.head = self.segments[0]
        self.head.shape("circle")
        self.head.color("green")
        self.head.shapesize(1.5)
        logger.info("Snake initialized with %d segments.", len(self.segments))

    def create_snake(self):
        """Create the initial snake using predefined starting positions."""

        for position in STARTING_POSITIONS:
            self.add_segment(position)

    def add_segment(self, position):
        """
        Add a new segment to the snake at the given position.

        Args:
            position (tuple): (x, y) coordinates for the new segment.
        """
        new_segment = self.turtle_factory("square")
        new_segment.color("green")
        new_segment.penup()
        new_segment.goto(position)
        self.segments.append(new_segment)

    def extend(self):
        """Add a segment to the end of the snake."""
        self.add_segment(self.segments[-1].position())
        logger.info("Snake extended. New length: %d", len(self.segments))

    def move(self):
        """Move the snake forward by updating segment positions."""
        for seg_num in range(len(self.segments) - 1, 0, -1):
            new_x, new_y = self.segments[seg_num - 1].position()
            self.segments[seg_num].goto(new_x, new_y)
        self.head.forward(MOVE_DISTANCE)
        logger.debug("Snake moved to head position: %s", self.head.position())

    def up(self):
        """Change the snake's direction to up, if not currently moving down."""
        if self.head.heading() != DOWN:
            self.head.setheading(UP)
            logger.debug("Snake direction changed to UP")

    def down(self):
        """Change the snake's direction to down, if not currently moving up."""
        if self.head.heading() != UP:
            self.head.setheading(DOWN)
            logger.debug("Snake direction changed to DOWN")

    def left(self):
        """Change the snake's direction to left, if not currently moving right."""
        if self.head.heading() != RIGHT:
            self.head.setheading(LEFT)
            logger.debug("Snake direction changed to LEFT")

    def right(self):
        """Change the snake's direction to right, if not currently moving left."""
        if self.head.heading() != LEFT:
            self.head.setheading(RIGHT)
            logger.debug("Snake direction changed to RIGHT")
