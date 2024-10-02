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
        type(self).number_of_instances += 1
        self.width = width
        self.height = height

    number_of_instances = 0
    print_symbol = "#"

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

    def area(self):
        """Returns the area of the rectangle"""
        return self.__width * self.__height

    def perimeter(self):
        """Returns the parameter of the rectangle"""
        if self.__width == 0 or self.__height == 0:
            return 0

        return 2 * (self.__height + self.__width)

    def __str__(self):

        if self.__height == 0 or self.__width == 0:
            return ""

        row = str(self.print_symbol) * self.__width
        rectangle = (row + '\n') * self.height

        return rectangle.strip()

    def __repr__(self):
        return f"Rectangle({self.__width}, {self.__height})"

    def __del__(self):
        type(self).number_of_instances -= 1
        print("Bye rectangle...")
# does not need an instance (anytime i dont need an instance i create static) if i realize taht i need attributes ill make it not static 
    @staticmethod
    def bigger_or_equal(rect_1, rect_2):

        if not isinstance(rect_1, Rectangle):
            raise TypeError("rect_1 must be an instance of Rectangle")
        if not isinstance(rect_2, Rectangle):
            raise TypeError("rect_2 must be an instance of Rectangle")

        if rect_1.area() >= rect_2.area():
            return rect_1
        else:
            return rect_2

    @classmethod
    def square(cls, size=0):
        return cls(size, size)
