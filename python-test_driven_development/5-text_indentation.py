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

    # Insert two newlines immediately after the target punctuation marks
    formatted_text = (
        text.replace('.', '.\n\n')
        .replace('?', '?\n\n')
        .replace(':', ':\n\n')
    )

    # Split the formatted text by newlines to process each line individually
    lines = formatted_text.split('\n')

    # Iterate through each line, strip leading/trailing spaces, and print
    for i in range(len(lines)):
        if i == len(lines) - 1:
            print(lines[i].strip(), end="")
        else:
            print(lines[i].strip())
