#!/usr/bin/python3
"""
This module provides a function `text_indentation` that formats a string
by adding 2 newlines after specific punctuation marks.
"""


def text_indentation(text):
    """
    Prints a text with 2 new lines after each of these characters: ., ? and :

    Args:
        text (str): The text to be formatted.

    Raises:
        TypeError: If text is not a string.
    """
    if type(text) is not str:
        raise TypeError("text must be a string")

    i = 0
    while i < len(text):
        # Skip spaces at the beginning of a line
        while i < len(text) and text[i] == ' ':
            i += 1

        if i == len(text):
            break

        # Accumulate characters for the current line
        line = ""
        while i < len(text) and text[i] not in ['.', '?', ':']:
            line += text[i]
            i += 1

        # If we stopped because of a punctuation mark
        if i < len(text) and text[i] in ['.', '?', ':']:
            line += text[i]
            i += 1
            print(line.strip())
            print()
        else:
            # Reached the end of the string without hitting punctuation
            print(line.strip(), end="")
