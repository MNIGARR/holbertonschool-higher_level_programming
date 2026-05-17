#!/usr/bin/python3
"""Module that defines shapes using abstract base classes and duck typing."""

from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """Abstract base class for shapes."""

    @abstractmethod
    def area(self):
        """Return the area of the shape."""
        pass

    @abstractmethod
    def perimeter(self):
        """Return the perimeter of the shape."""
        pass


class Circle(Shape):
    """Circle class."""

    def __init__(self, radius):
        """Initialize circle with radius."""
        self.radius = abs(radius)

    def area(self):
        """Return area of circle."""
        return math.pi * self.radius ** 2

    def perimeter(self):
        """Return perimeter of circle."""
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """Rectangle class."""

    def __init__(self, width, height):
        """Initialize rectangle with width and height."""
        self.width = width
        self.height = height

    def area(self):
        """Return area of rectangle."""
        return self.width * self.height

    def perimeter(self):
        """Return perimeter of rectangle."""
        return 2 * (self.width + self.height)


def shape_info(shape):
    """Print area and perimeter of any shape (duck typing)."""
    print("Area: {}".format(shape.area()))
    print("Perimeter: {}".format(shape.perimeter()))
