#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ A class used to define a square"""

    def __init__(self, size=0):
        """Initialize the square with a private instance attribute

        Args:
        size: The size of the square
        """
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        if size < 0:
            raise ValueError("size must be >= 0")

        self.__size = size

    def area(self):
        """Returns the current square area"""
        return self.__size ** 2
