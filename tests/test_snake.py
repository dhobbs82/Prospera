"""
Unit tests for the Snake class using a DummyTurtle.

Tests the basic behavior of the snake, including movement,
segment extension, and direction changes.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from src.snake import Snake, MOVE_DISTANCE, UP, DOWN, LEFT, RIGHT
from src.dummy_turtle import DummyTurtle


def make_snake():
    """
    Create a Snake instance using DummyTurtle for testing.

    Returns:
        Snake: A Snake object with 3 initial segments.
    """
    return Snake(turtle_factory=DummyTurtle)


def test_snake_starts_with_three_segments():
    """Test that a new snake has three segments and head at (0, 0)."""
    snake = make_snake()
    assert len(snake.segments) == 3
    assert snake.head.position() == (0.0, 0.0)


def test_snake_extend_increases_length():
    """Test that extending the snake adds a segment."""
    snake = make_snake()
    initial_len = len(snake.segments)
    snake.extend()
    assert len(snake.segments) == initial_len + 1


def test_snake_move_changes_head_position():
    """Test that moving the snake updates the head's position."""
    snake = make_snake()
    x0, y0 = snake.head.position()
    snake.move()
    x1, y1 = snake.head.position()
    assert (x1, y1) != (x0, y0)


def test_snake_segments_follow_head():
    """Test that segments correctly follow the head after a move."""
    snake = make_snake()
    initial_positions = [seg.position() for seg in snake.segments]
    snake.move()
    new_positions = [seg.position() for seg in snake.segments]
    assert new_positions[1] == initial_positions[0]


def test_snake_direction_change():
    """Test that the snake changes direction correctly and prevents reversal."""
    snake = make_snake()
    snake.up()
    assert snake.head.heading() == UP
    snake.down()
    # Reversal is not allowed; heading should remain UP
    assert snake.head.heading() == UP
