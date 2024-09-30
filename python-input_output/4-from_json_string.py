#!/usr/bin/python3
"""Defines a function that returns an object"""
import json


def from_json_string(my_str):
    """Returns an object(Python data structure)
    represented by a JSON string
    Args:
        my_str: Object to be parsed
    """
    return json.loads(my_str)
