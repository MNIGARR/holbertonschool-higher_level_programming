#!/usr/bin/python3
"""Module that defines an abstract Animal class and its subclasses."""

from abc import ABC, abstractmethod


class Animal(ABC):
    """Abstract base class Animal."""

    @abstractmethod
    def sound(self):
        """Return the sound of the animal."""
        pass


class Dog(Animal):
    """Dog class that inherits from Animal."""

    def sound(self):
        """Return dog sound."""
        return "Bark"


class Cat(Animal):
    """Cat class that inherits from Animal."""

    def sound(self):
        """Return cat sound."""
        return "Meow"
