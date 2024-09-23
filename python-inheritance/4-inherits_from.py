#!/usr/bin/python3
"""Defines a function that checks if an object is an instance of a class
that inherited from another class, but not directly the class itself"""


def inherits_from(obj, a_class):
    """Returns True if the object is an instance of a class that inherited
    (directly or indirectly) from the specified class

    Parameters:
    obj: The object to check.
    a_class: The class to compare against.

    Returns:
    True if obj is an instance of a_class or a subclass, otherwise False.
    """""
    if isinstance(obj, a_class) and type(obj) != a_class:
        return True
    else:
        return False
