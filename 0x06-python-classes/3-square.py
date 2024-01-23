#!/usr/bin/python3
class Square:
    """
    Defines a square.

    Attributes:
    - size (int): The size of the square.
    """
    def __init__(self, size=0):
        """
        Initializes a new square instance.

        Parameters:
        - size (int, optional): The size of the square (default is 0).
        """
        if type(size) is not int:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >=0")
        else:
            self.__size = size

    def area(self):
        """
        Calculates and returns the current square area.

        Returns:
        - int: The area of the square.
        """
        return self.__size ** 2
