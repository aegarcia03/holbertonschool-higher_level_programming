#!/usr/bin/python3
import json
"""Defines a function that returns the JSON representation"""


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj: A string
    Retunrs:
        The JSON representation of my_obj"""
    return json.dumps(my_obj)
