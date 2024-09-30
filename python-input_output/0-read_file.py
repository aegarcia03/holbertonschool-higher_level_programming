#!/usr/bin/python3
"""Defines a text file-reading function"""


def read_file(filename=""):
    """Print the content of a UTF8 file in stdout
    Args:
        filename: text
    """
    with open(filename, 'r', encoding="utf-8") as file:
        for lines in file:
            print(lines.strip())
