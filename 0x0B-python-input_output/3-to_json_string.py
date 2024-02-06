#!/usr/bin/pyhton3
"""Defines a function that converts python object to JSON representation."""


# Import the json module:
import json
def to_json_string(my_obj):
    """
    A function to return a JSON representation of an object string.

    Args:
        my_obj (str): object to be converted to JSON string.

    Return:
        JSON string.
    """
    y = json.dumps(my_obj)
    """Assigns the converted python string to y."""
    return y
