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
        all_attr = self.__dict__
        filtered_attr = {}

        if isinstance(attrs, list):
            for attr in attrs:
                if isinstance(attr, str) and attr in all_attr:
                    filtered_attr[attr] = all_attr[attr]
            return filtered_attr
        return all_attr
