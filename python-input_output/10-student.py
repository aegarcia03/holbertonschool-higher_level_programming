#!/usr/bin/python3
"""This module defines a "Student" class"""


class Student:
    """
    A class used to define Student

    Attributes:
        first_name
        last_name
        age
    Methods: ...
    ____________"""
    def __init__(self, first_name, last_name, age):
        """Instantiation with first name, last name and age.
        """
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        """Retrieves a dictionary representation of a Student instance"""
        if type(attrs) == list
            return
        else:
            return self.__dict__
