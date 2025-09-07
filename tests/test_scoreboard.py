"""
Unit tests for the Scoreboard class using DummyTurtle.

Tests initial score, score increment, and game over message.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from src.scoreboard import Scoreboard
from src.dummy_turtle import DummyTurtle


def test_scoreboard_starts_at_zero():
    """Test that a new Scoreboard starts with a score of 0."""
    board = Scoreboard(turtle_factory=DummyTurtle)
    assert board.score == 0


def test_increase_score_increments_value():
    """Test that increasing the score updates the score value."""
    board = Scoreboard(turtle_factory=DummyTurtle)
