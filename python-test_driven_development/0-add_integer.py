#!/usr/bin/python3
"""
This module supplies one function, add_integer().
The addition between two numbers,
these numbers can be integers or floats. For example,
>>> add_integer(1, 2)
3
"""


def add_integer(a, b=98):
    """
    Performs the addition of two numbers

    Parameters:
    a(int, float): The first number
    b(int, float, optional): The second number. Defaults to 98

    Returns:
        int: The sum of a and b. Cast to an integer
    Raises:
        TypeError: if a or b is not an int or float
    """

    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
