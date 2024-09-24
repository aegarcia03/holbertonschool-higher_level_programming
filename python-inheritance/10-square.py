#!/usr/bin/python3
"""Defines a class Square that inherits from Rectangle"""


Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Is a subclass of Rectangle

    Atributes
        None
    """
    def __init__(self, size):
        """Initialize a new Square

        Args:
            size(int): The size of the Square
        """
        self.integer_validator("size", size)
        self.__size = size
        super().__init__(size, size)

    def area(self):
        """Returns the area of the rectangle"""
        return self.__size ** 2
