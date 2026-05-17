#!/usr/bin/python3
"""Defines a Square class."""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """Represents a Square class that inherits from Rectangle class."""

    def __init__(self, size):
        """Initiates a constructor with private attribute size."""
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
