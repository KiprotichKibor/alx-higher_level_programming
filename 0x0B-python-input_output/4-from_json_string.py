#!/usr/bin/python3
"""Defines a function that returns object represented by JSON string."""
import json


def from_json_string(my_str):
    """
    Parse JSON string.

    args:
        my_str (str): json string to be converted to python string.

    Returns:
        Python string.
    """
    return json.loads(my_str)
