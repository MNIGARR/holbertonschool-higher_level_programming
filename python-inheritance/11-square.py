#!/usr/bin/python3
"""Module that defines the Square class."""

Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Class that defines a square."""

    def __init__(self, size):
        """Initialize a square with size."""
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def __str__(self):
        """Return the string representation of the square."""
        return "[Square] {}/{}".format(
            self._Rectangle__width,
            self._Rectangle__height
        )
