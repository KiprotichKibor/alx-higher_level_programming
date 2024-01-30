#!/usr/bin/python3
def print_square(size):
    """
    Prints a square with the character #.

    parameters:
    size (int): The size lenght of the square.

    Raises:
    TypeError: I f size is not an integer.
    ValueError: If size is less than 0.
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    """check if size is an integer"""

    if size < 0:
        raise ValueError("size must be >= 0")
    """check if size is less than zero"""

    for _ in range(size):
        print("#" * size)
    """print the square with # character"""
