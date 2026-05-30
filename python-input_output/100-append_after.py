#!/usr/bin/python3
"""Module that defines a function to insert text after a specific string."""


def append_after(filename="", search_string="", new_string=""):
    """
    Inserts a line of text to a file, after each line containing
    a specific string.

    Args:
        filename (str): The name of the file.
        search_string (str): The string to search for within the file.
        new_string (str): The string to append after the matching line.
    """
    lines = []
    with open(filename, "r", encoding="utf-8") as f:
        for line in f:
            lines.append(line)
            if search_string in line:
                lines.append(new_string)

    with open(filename, "w", encoding="utf-8") as f:
        f.writelines(lines)
