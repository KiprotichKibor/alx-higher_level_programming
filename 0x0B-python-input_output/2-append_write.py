#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file."""


def append_write(filename="", text=""):
    """
    Appends a string to a UTF8 text file.

    Args:
        filename (str): The file to be appended.
        text (str): The text to be appended.

    Return:
        The number of characters added.
    """
    with open(filename, "a", encoding="utf-8") as f:
        """Appends texts to file and returns the num of text added."""
        return f.write(text)
