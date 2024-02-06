#!/usr/bin/python3
"""Defines a function that writes an object to text file using JSON string."""
import json


def save_to_json_file(my_obj, filename):
    """
    A function to write object to filename using JSON representation.

    Args:
        my_obj (str): objects to be saved in json string
        filename (str): the name of the text file
    """
    with open(filename, "w", encoding="utf-8") as f:
        """opens file for writing."""
        json.dump(my_obj, f)
