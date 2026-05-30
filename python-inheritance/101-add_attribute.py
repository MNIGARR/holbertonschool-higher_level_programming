#!/usr/bin/python3
"""Module that defines a function to add attributes to objects."""


def add_attribute(obj, attribute, value):
    """
    Adds a new attribute to an object if it's possible.

    Args:
        obj (any): The object to add the attribute to.
        attribute (str): The name of the attribute to add.
        value (any): The value of the attribute.

    Raises:
        TypeError: If the object cannot have new attributes added.
    """
    if not hasattr(obj, "__dict__"):
        raise TypeError("can't add new attribute")
    setattr(obj, attribute, value)
