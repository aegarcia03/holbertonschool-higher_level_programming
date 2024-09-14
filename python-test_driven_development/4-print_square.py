#!/usr/bin/python3
"""Prints a square pattern with the character #"""


def print_square(size):
    """Prints a square pattern with the character #

    Parameters:
    size: is the lenght of the square

    Raises:
    TypeError: if size is not an integer
    ValueError: if size is less than 0
    TypeError: if size is a float or less than 0
    """

    if not isinstance(size, int):
        raise TypeError("size must be an integer")
    if size < 0:
        raise ValueError("size must be >= 0")

    for i in range(size):
        for j in range(size):
            print("#", end='')
        print()
