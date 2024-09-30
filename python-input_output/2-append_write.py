#!/usr/bin/python3
"""Defines a function that appends a string at the end of a text file"""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename: Text file UTF8
        text: String to append
    Returns:
        The number of characters added"""

    with open(filename, 'a', encoding="UTF8") as file:
        app_characters = file.write(text)
        return app_characters
