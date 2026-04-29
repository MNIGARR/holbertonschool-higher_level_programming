#!/usr/bin/python3
"""
0. Integers addition
"""


def add_integer(a, b=98):
    """
    Returns the addition of a and b.
    a and b must be integers or floats; otherwise, raises TypeError.
    Floats are casted to integers before addition.
    """
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if a != a or a in (float('inf'), float('-inf')):
        raise TypeError("a must be an integer")
    if b != b or b in (float('inf'), float('-inf')):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
