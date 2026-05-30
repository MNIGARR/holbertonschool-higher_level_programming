#!/usr/bin/python3
"""Module that defines a rebel integer class MyInt."""


class MyInt(int):
    """
    A class that inherits from int but inverts the standard
    equality (==) and inequality (!=) operators.
    """

    def __eq__(self, other):
        """
        Inverts the == operator to behave like !=.
        """
        return super().__ne__(other)

    def __ne__(self, other):
        """
        Inverts the != operator to behave like ==.
        """
        return super().__eq__(other)
