#!/usr/bin/env python3
"""This module provides functions to serialize a Python dictionary to a JSON file
and deserialize the JSON file back into a Python dictionary"""
import json


def serialize_and_save_to_file(data, filename):
    """
    Serializes a Python dictionary into a JSON format and saves it to a file.
    
    Parameters:
        data (dict): The Python dictionary to be serialized.
        filename (str): The name of the output JSON file where 
        the serialized data will be saved.
        """
    with open(filename, 'w') as file:
        json_str = json.dump(data, file)


def load_and_deserialize(filename):
    """
    Loads data from a JSON file and deserializes it back into a Python dictionary.
    
    Parameters:
        filename (str): The name of the input JSON file containing the serialized data.
        
    Returns:
        dict: A Python dictionary deserialized from the JSON file.
    """
    with open(filename, 'r') as file:
        return json.load(file)
