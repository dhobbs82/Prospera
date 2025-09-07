"""
Dummy Turtle class for testing purposes.

Simulates a Turtle object without rendering graphics, allowing unit tests
to run without opening a GUI window.

Group Prospera
Authors: 

Brunner, John
Carrol, Josh
Hobbs, Derrick
Montgomery, Samuel
Reece, Manu
"""


class DummyTurtle:
    """A mock Turtle object for testing Snake game logic."""

    def __init__(self, shape="square"):
        """
        Initialize a DummyTurtle.

        Args:
            shape (str, optional): Initial shape of the turtle. Defaults to "square".
        """
        self._pos = (0.0, 0.0)
        self._heading = 0
        self._shape = shape
        self._color = None
        self._size = None
        self._hidden = False
        self._written = []

    def position(self):
        """Return the current position as an (x, y) tuple."""
        return self._pos

    def goto(self, x, y=None):
        """
        Move the turtle to a specified position.

        Args:
            x (float or tuple): x-coordinate or a tuple (x, y)
            y (float, optional): y-coordinate if x is not a tuple.
        """
        if isinstance(x, tuple):
            self._pos = x
        else:
            self._pos = (x, y)

    def forward(self, distance):
        """
        Move the turtle forward in the direction of the current heading.

        Args:
            distance (float): Distance to move.
        """
        x, y = self._pos
        if self._heading == 0:  # right
            self._pos = (x + distance, y)
        elif self._heading == 180:  # left
            self._pos = (x - distance, y)
        elif self._heading == 90:  # up
            self._pos = (x, y + distance)
        elif self._heading == 270:  # down
            self._pos = (x, y - distance)

    def heading(self):
        """Return the current heading in degrees."""
        return self._heading

    def setheading(self, heading):
        """
        Set the turtle's heading.

        Args:
            heading (int): New heading in degrees.
        """
        self._heading = heading

    def penup(self):
        """Simulate lifting the pen (no-op)."""
        pass

    def color(self, *args):
        """Set the turtle's color."""
        self._color = args

    def shape(self, *args):
        """Set the turtle's shape."""
        self._shape = args

    def shapesize(self, *args):
        """Set the turtle's size."""
        self._size = args

    def hideturtle(self):
        """Hide the turtle (simulation)."""
        self._hidden = True

    def write(self, text, **kwargs):
        """
        Simulate writing text with the turtle.

        Args:
            text (str): Text to write.
            **kwargs: Optional writing arguments.
        """
        self._written.append((text, kwargs))

    def clear(self):
        """Clear all written text."""
        self._written.clear()

    def speed(self, *args):
        """Simulate setting turtle speed (no-op)."""
        pass
