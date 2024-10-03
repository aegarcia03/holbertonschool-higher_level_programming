#!/usr/bin/env python3
"""This module provides functions to serialize a Python dictionary
and deserialize the JSON file with the pickle module"""
import pickle


class CustomObject:

    def __init__(self, name, age, is_student):
        self.name = name
        self.age = age
        self.is_student = is_student

    def display(self):
        """Display the attributes of the object."""
        print(f"Name: {self.name}")
        print(f"Age: {self.age}")
        print(f"Is Student: {self.is_student}")

    def serialize(self, filename):
        """Serialize the current instance to a file."""
        try:
            with open(filename, mode="wb") as file:
                pickle_str = pickle.dump(self, file)
        except IOERROR:
            return None

    @classmethod
    def deserialize(cls, filename):
        """Deserialize an object from a file."""
        try:
            with open(filename, mode="rb") as file:
                return pickle.load(file)
        except FileNotFoundError:
            return None
