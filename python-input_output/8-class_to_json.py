#!/usr/bin/python3
"""Defines a class-to-JSON function"""


def class_to_json(obj):
    """Returns the dictionary description with simple data structure
    Args:
        obj: instance of a class"""
    return obj.__dict__
