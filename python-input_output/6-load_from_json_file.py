#!/usr/bin/python3
"""Defines a JSON file-reading function"""
import json


def load_from_json_file(filename):
    """Creates an Object from a JSON file
    Args:
        filename(str): text file"""
    with open(filename, mode='r') as file:
        return json.load(file)
