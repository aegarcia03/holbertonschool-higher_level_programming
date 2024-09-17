#!/usr/bin/python3
"""This module defines a 'Rectangle' class that represents a rectangle shape"""


class Rectangle:
    """
    A class used to define a rectangle

    Attributes: ...
    ------------
    Methods: ...
    ---------
    """
    def __init__(self, width=0, height=0):
        """Initialazes the rectangle with the specified width and height.

        Args:
        ----
        width: The width of the rectangle
        height: The height of the rectangle.

        Raises:
        ------
        TypeError: if 'width' or 'height' is not an integer
        ValueError: if 'width' or 'height' is less than 0.
        """
        self.width = width
        self.height = height

    @property
    def width(self):
        return self.__width

    @width.setter
    def width(self, value):

        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")

        self.__width = value

    @property
    def height(self):
        return self.__height

    @height.setter
    def height(self, value):

        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")

        self.__height = value
