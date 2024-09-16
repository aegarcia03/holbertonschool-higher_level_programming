#!/usr/bin/python3
"""Defines a square"""


class Square:
    """ A class used to define a square"""

    def __init__(self, size):
        """Initialize the square with a private instance attribute

        Args:
        size: The size of the square
        """
        self.__size = size
