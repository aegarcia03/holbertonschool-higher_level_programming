#!/usr/bin/python3
"""Defines a list"""


class MyList(list):
    """
    MyList is a custom list class that inherits from the buil-in list.

    Atributes
        None
    """
    def print_sorted(self):
        """Prints the list in ascending order
        The original list remains unchanged (sorted)
        """
        sorted_list = sorted(self)
        print(sorted_list)
