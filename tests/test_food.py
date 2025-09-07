"""
Unit tests for the Food class using a DummyTurtle.

Tests food placement, position, and alignment to the grid.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""

from src.food import Food, get_location
from src.dummy_turtle import DummyTurtle


def make_food():
    """
    Create a Food instance using DummyTurtle for testing.

    Returns:
        Food: A Food object.
    """
    return Food(turtle_factory=DummyTurtle)


def test_food_has_position_methods():
    """Test that Food exposes xcor, ycor, and position methods."""
    food = make_food()
    pos = food.position()
    x = food.xcor()
    y = food.ycor()
    assert pos == (x, y)


def test_get_location_grid_alignment():
    """
    Test that get_location() returns a value aligned to 20px grid
    and within the allowed range.
    """
    for _ in range(50):
        loc = get_location()
        # Grid alignment: should be multiple of 20
        assert loc % 20 == 0
        # Position within bounds
        assert -270 <= loc <= 270


def test_food_refresh_changes_position():
    """Test that refreshing the food changes its position."""
    food = make_food()
    old_pos = food.position()
    food.refresh()
    new_pos = food.position()
    # With random, possible to get same position, so repeat if needed
    attempts = 5
    changed = old_pos != new_pos
