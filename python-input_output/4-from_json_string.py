#!/usr/bin/python3
"""Import JSON module"""
import json


def from_json_string(my_str):
    """deserialization"""
    return json.loads(my_str)
