#!/usr/bin/python3
"""A class that defines a rectagle"""


class Rectangle:
    """
    A class representing a rectangle

    Attributes:
    __width (int): The width of the rectangle
    __height (int): The height of the rectangle

    Methods:
    __init__: Initialize a Rectangle object with optional width and height
    width: Getter method for retrieving the width of the rectangle
    height: Getter method for retrieving the height of the rectangle
    width.setter: Setter method for setting the width of the rectangle
    height.setter: Setter method for setting the hight of the rectangle
    """

    def __init__(self, width=0, height=0):
        """
        Initialize a Rectangel object with optional width and height.

        Args:
            width (int): The width of the rectangle (default 0).
            height (int): The height of the rectangle (default 0).
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        """Get the width of the rectangle."""
        return self.__width

    @width.setter
    def width(self, value):
        """Set the width of the rectangle.

        Args:
            Value (int): The new width of the rectangle.

        Raises:
            TypeError: If the width is not an integer.
            ValueError: If the width is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        elif value < 0:
            raise ValueError("width must be >= 0")
        else:
            self.__width = value

    @property
    def height(self):
        """Get the height of the rectangle."""
        return self.__height

    @height.setter
    def height(self, value):
        """
        Set the height of the rectangle.

        Args:
            Value (int): The new height of the rectangle.

        Raises:
            TypeError: If the height is not an integer.
            ValueError: If the height is less than 0.
        """
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        elif value < 0:
            raise ValueError("height must be >= 0")
        else:
            self.__height = value
