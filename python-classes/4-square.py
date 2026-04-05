#!/usr/bin/python3
"""Module that defines a square."""


class Square:
    """A class that represents a square."""

    def __init__(self, size=0):
        """Initialize a new Square.

        Args:
            size (int): The size of the new square. Defaults to 0.
        """
        # Assigning to self.size automatically calls the setter method
        self.size = size

    @property
    def size(self):
        """Retrieve the size of the square."""
        return self.__size

    @size.setter
    def size(self, value):
        """Set the size of the square with validation.

        Args:
            value (int): The new size to be assigned.

        Raises:
            TypeError: If value is not an integer.
            ValueError: If value is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        
        self.__size = value

    def area(self):
        """Calculate and return the area of the square.

        Returns:
            int: The current area of the square.
        """
        return self.__size ** 2
    