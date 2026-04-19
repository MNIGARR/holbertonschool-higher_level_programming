#!/usr/bin/python3
"""Function appends text to a file."""


def append_write(filename="", text=""):
    """Appends a string to text file and returns characters added."""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
