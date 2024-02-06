#!/usr/bin/python3
"""Defines a function that creates an object from JSON file."""
import json


def load_from_json_file(filename):
    """
    Creates a python file from JSON file.

    Args:
        filename (str): the file where python file will be saved
    """
    with open(filename) as f:
        """creates a file."""
        return json.load(f)
