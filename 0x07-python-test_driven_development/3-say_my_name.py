#!/usr/bin/python3
def say_my_name(first_name, last_name=""):
    """
    Prints "My name is <first name> <last name>".

    Parameters:
    first_name (str): The first name.
    last_name (str, optional): The last name defaults to "".

    Returns:
    str: The formatted string.

    Raises:
    TypeError: If fisrt_name or last_name is not a string.
    """

    if not isinstance(first_name, str) or not isinstance(last_name, str):
        raise TypeError("first_name must be a string or last_name must be a string")
    """check if first_name and last_name are strings"""

    if last_name:
        return f"My name is {first_name} {last_name}"
    else:
        return f"My name is {first_name}"
    """construct and return the formatted string"""
