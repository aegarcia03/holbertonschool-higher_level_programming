#!/usr/bin/python3
"""Defines a file-appending function""


def append_write(filename="", text=""):
    """Appends a string at the end of a text file
    Args:
        filename(str): Text file
        text(str): String to append
    Returns:
        The number of characters added"""

    with open(filename, 'a', encoding="UTF8") as file:
        app_characters = file.write(text)
        return app_characters
