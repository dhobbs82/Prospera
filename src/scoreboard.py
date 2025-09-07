"""
Module for the Scoreboard class used in the Snake game.

Provides functionality to display and update the player's score
and show the game over message.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from turtle import Turtle

ALIGNMENT = "center"
FONT = ("Arial", 24)


class Scoreboard:
    """
    Represents the game scoreboard.

    Attributes:
        _turtle (Turtle): Internal Turtle object used to display text.
        score (int): The current score of the game.
    """

    def __init__(self, turtle_factory=Turtle):
        """
        Initialize a Scoreboard object and display the starting score.

        Args:
            turtle_factory (callable, optional): Factory function to create Turtle.
                Defaults to the Turtle class.
        """
        self._turtle = turtle_factory()
        self._turtle.hideturtle()
        self._turtle.color("white")
        self._turtle.penup()
        self._turtle.goto(0, 270)
        self.score = 0
        self.update_scoreboard()

    def update_scoreboard(self):
        """
        Update the scoreboard display with the current score.
        """
        self._turtle.write(f"Score: {self.score}", align=ALIGNMENT, font=FONT)

    def game_over(self):
        """
        Display the "GAME OVER" message at the center of the screen.
        """
        self._turtle.goto(0, 0)
        self._turtle.write("GAME OVER", align=ALIGNMENT, font=FONT)

    def increase_score(self):
        """
        Increase the score by one and update the display.
        """
        self.score += 1
        self._turtle.clear()
        self.update_scoreboard()

    def position(self):
        """
        Get the current position of the scoreboard turtle.

        Returns:
            tuple: (x, y) coordinates of the turtle.
        """
        return self._turtle.position()
