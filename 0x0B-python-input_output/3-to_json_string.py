#!/usr/bin/pyhton3
# Import the json module:
import json

"""Defines a function that converts python object to JSON representation."""


def to_json_string(my_obj):
    """
    A function to return a JSON representation of an object string.

    Args:
        my_obj (str): object to be converted to JSON string.

    Return:
        JSON string.
    """
    y = json.dumps(my_obj)
    """Assigns y the converted python string."""
    return y
