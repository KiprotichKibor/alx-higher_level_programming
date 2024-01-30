#!/usr/bin/python3
def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix.

    Parameters:
    matrix (list of lists): The matrix containing integers or floats.
    div (int or float): The divisor.

    Returns:
    list of lists: A new matrix with elements divided by div, rounded to 2

    Raises:
    TypeError: If matrix is not a list of integers or floats.
    TypeError: If eah row of the matrix does not have the same size.
    TypeError: If div is not a number (integer or float).
    ZeroDivisionError: If div is equal to 0.
    """

    if not all(isinstance(row, list) and all(isinstance(elem, (int, float))for elem in row)for row in matrix):
        raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    """Check if matrix is a list of lists of integers or floats"""

    if not all(len(row) == len(matrix[0]) for row in matrix):
        raise TypeError("Each row of the matrix must have the same size")
    """check if each row of the matrix has the same size"""

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    """check if div is a number (integer or float)"""

    if div == 0:
        raise ZeroDivisionError("division by zero")
    """check if is not equal to 0"""

    return [[round(elem / div, 2) for elem in row] for row in matrix]
    """Divide all elements of the matrix by div, rounded to 2 decimal places""" 
