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

    def my_print(self):
        """the square with the character #"""
        if self.__size == 0:
            print("")
        else:
            for i in range(self.__size):
                print("#" * self.__size)
