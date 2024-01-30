#!/usr/bin/python3
def add_integer(a, b=98):
    """
    Adds two integers.

    Parameters:
    a (int or float): The first number.
    b (int or float, optional): The second number. Defaults to 98.

    Returns:
    int: The sum of a and b as integers.

    Raises:
    TypeError: If a or b is not an integer or float.
    """

    if not isinstance(a, (int, float)) or not isinstance(b, (int, float)):
        raise TypeError("a must be an integer or b must be an integer")
    """ Check if a and b are integers or floats """

    a = int(a)
    b = int(b)
    """ Convert a and b to integers if they are floats """

    return a + b
    """ Add a and b and return the result """
