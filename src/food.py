"""
Module for the Food class used in the Snake game.

Provides functionality to create a food object, place it randomly on the screen,
and expose position helpers for game logic and testing.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from turtle import Turtle
import random
import math

def get_location():
    """
    Generate a random grid-aligned coordinate between -270 and 270.

    Returns:
        int: A coordinate aligned to the 20x20 grid.
    """
    result = random.randint(-270, 270)
    # Align to 20-pixel grid and clamp to bounds
    result = max(-270, min(270, math.ceil(result / 20) * 20))
    return result


class Food:
    """
    Represents a food object in the Snake game.

    Attributes:
        _turtle (Turtle): Internal Turtle object used to display the food.
    """

    def __init__(self, turtle_factory=Turtle):
        """
        Initialize a Food object and place it at a random location.

        Args:
            turtle_factory (callable, optional): Factory function to create Turtle.
                Defaults to the Turtle class.
        """
        self._turtle = turtle_factory("turtle")
        self._turtle.penup()
        self._turtle.shapesize(1)
        self._turtle.color("blue")
        self._turtle.speed("fastest")
        self.refresh()

    def refresh(self):
        """
        Move the food to a new random location on the screen.
        """
        self._turtle.goto(get_location(), get_location())

    def position(self):
        """
        Get the current position of the food.

        Returns:
            tuple: (x, y) coordinates of the food.
        """
        return self._turtle.position()

    def xcor(self):
        """
        Get the x-coordinate of the food.

        Returns:
            float: X position.
        """
        return self._turtle.position()[0]

    def ycor(self):
        """
        Get the y-coordinate of the food.

        Returns:
            float: Y position.
        """
        return self._turtle.position()[1]
