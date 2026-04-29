#!/usr/bin/python3
"""This module defines a square."""


class Square:
    """Defines a square."""
    def __init__(self, size=0):
        self.__size = size

    @property
    def size(self):
        """The getter method."""
        return self.__size

    @size.setter
    def size(self, value):
        """The setter method with validation."""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        if value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    def area(self):
        """Defines an area."""
        area = self.__size**2
        return area
