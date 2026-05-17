#!/usr/bin/python3
"""
    Module that defines a function to check if an object is
    an instance of a class that inherited (directly or indirectly) from the specified class.
"""


def is_kind_of_class(obj, a_class):
    """
    Return True if obj is an instance of a_class or a class that inherited from a_class,
    otherwise return False.
    """
    return isinstance(obj, a_class)
