#!/usr/bin/python3
"""
This module supplies one function, matrix_divided().
The division of all elements of a matrix by one number,
this number can be integer or float.
"""


def validate_matrix(matrix):

    if not isinstance(matrix, list):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    if not all(isinstance(row, list) for row in matrix):
        raise TypeError(
            "matrix must be a matrix (list of lists) of integers/floats"
            )
    for row in matrix:
        if not all(isinstance(element, (int, float)) for element in row):
            raise TypeError(
                "matrix must be a matrix (list of lists) of integers/floats"
                )

    return True


def size_row(matrix):
    lenght = len(matrix[0])
    for row in matrix:
        if len(row) != lenght:
            raise TypeError("Each row of the matrix must have the same size")

    return True


def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by a number and rounds the result to
    two decimals

    Parameters:
    matrix (lists of lists of int/float): The matrix to be divided
    div (int/float): The divisor

    Returns:
    Lists of lists of float: The resulting matrx after division

    Raises:
    TypeError: If div is not a number
    If matrix is not a list of lists of int/float
    ZeroDivisionError: If div is zero
    """
    validate_matrix(matrix)
    size_row(matrix)

    result = [[0 for _ in range(len(row))] for row in matrix]

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")
    if div == 0:
        raise ZeroDivisionError("division by zero")

    for i in range(len(matrix)):
        for j in range(len(matrix[i])):
            result[i][j] = round(matrix[i][j] / div, 2)

    return result
