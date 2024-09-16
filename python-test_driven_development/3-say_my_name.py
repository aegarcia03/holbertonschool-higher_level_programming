#!/usr/bin/python3
"""Prints "My name is <first_name> <last_name>"""


def say_my_name(first_name, last_name=""):
    """Prints "My name is <first_name> <last_name>"

    Parameters:
    first_name(str): The first name
    last_name(str, optional): The last name. Defaults to an empty string.

    Returns:
        None: This function only prints the formatted string

    Raises:
        TypeError: if the arguments are not a string
    """
    if not isinstance(first_name, str):
        raise TypeError("first_name must be a string")
    if not isinstance(last_name, str):
        raise TypeError("last_name must be a string")
    
    if last_name:
        print("My name is {} {}".format(first_name, last_name))
    else:
        print("My name is {}".format(first_name))
