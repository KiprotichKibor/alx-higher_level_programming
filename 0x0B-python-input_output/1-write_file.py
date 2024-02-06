#!/usr/bin/python3
"""Defines a function that writes to a file."""


def write_file(filename="", text=""):
    """Opens the file for writing.

    Args:
        filename (str): The name of the file to write.
        text (str): The text to write to the file.

    Returns:
        The number of the characters written.
    """
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
