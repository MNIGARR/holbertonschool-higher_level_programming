#!/usr/bin/python3
"""inherit"""


def inherits_from(obj, a_class):
    """inherit"""
    return isinstance(obj, a_class) and type(obj) is not a_class
