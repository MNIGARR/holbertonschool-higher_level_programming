#!/usr/bin/python3
"""This module defines a rectangle."""


class Rectangle:
    """Defines a rectangle."""
    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        """Defines an area."""
        area = self.__height*self.__width
        return area

    def perimeter(self):
        """Defines a perimeter."""
        if self.__height == 0 or self.__width == 0:
            return 0
        else:
            perimeter = 2*(self.__height+self.__width)
            return perimeter

    def __str__(self):
        """the rectangle with the character #"""
        if self.__height == 0 or self.__width == 0:
            return ""
        return "\n".join(["#" * self.__width for i in range(self.__height)])

    def __repr__(self):
        return "Rectangle({}, {})".format(self.__width, self.__height)

    def __del__(self):
        print("Bye rectangle...")
