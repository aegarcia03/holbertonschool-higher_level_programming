#!/usr/bin/python3
"""Defines a JSON file-writing function"""
import json


def save_to_json_file(my_obj, filename):
    """Writes an object to a text file using JSON representation
    Args:
        my_obj: Object to be written in text file
        filename: Text file"""

    with open(filename, 'w') as file:
        text = json.dump(my_obj, file)
