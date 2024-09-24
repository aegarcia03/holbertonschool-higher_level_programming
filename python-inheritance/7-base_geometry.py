#!/usr/bin/python3
"""Defines a geometry module"""


class BaseGeometry:
    """
    Is a class of Geometry

    Atributes
        None
    """

    def area(self):
        """Raises an Exception with a message"""
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        """Validates value as an integer

        Args:
            name(str): The name of the parameter
            value(int): The parameter to validate
        Raises:
            TypeError if value is not an integer
            ValueError if value not greater than zero
        """
        if type(value) != int:
            raise TypeError(f"{name} must be an integer")
        if value <= 0:
            raise ValueError(f"{name} must be greater than 0")
