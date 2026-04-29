#!/usr/bin/python3
"""import JSON module"""
import json


def save_to_json_file(my_obj, filename):
    """function writes object to atext file using JSON"""
    with open(filename, "w", encoding="utf-8") as f:
        return json.dump(my_obj, f)
