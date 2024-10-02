#!/usr/bin/python3
"""Defines a string-to-JSON"""
import json


def to_json_string(my_obj):
    """Returns the JSON representation of an object
    Args:
        my_obj: A string
    Retunrs:
        The JSON representation of my_obj"""
    return json.dumps(my_obj)
