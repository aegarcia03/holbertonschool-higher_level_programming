#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class"""


def is_kind_of_class(obj, a_class):
    """Returns True if the object is an instance of the specified class"""
    if not isinstance(obj, a_class):
        return False
    else:
        return True
