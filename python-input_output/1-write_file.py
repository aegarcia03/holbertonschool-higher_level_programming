#!/usr/bin/python3
"""Defines a file-writing function""


def write_file(filename="", text=""):
    """Writes a string to a text file UTF8
    Args:
        filename: text file UTF8
        text: string to write in the file
    Returns:
        The number of characters written"""

    with open(filename, 'w', encoding="UTF8") as file:
        num_characters = file.write(text)
        return num_characters
