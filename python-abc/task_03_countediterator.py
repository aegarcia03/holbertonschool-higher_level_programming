#!/usr/bin/env python3
"""Defines a counter iterator"""


class CountedIterator:
    """A class that extends the built-in iterator obtained from the
    iter function"""

    def __init__(self, some_iterable):
        """Initializes the CountedIterator
        Args:
            some_iterable: any iterable object (e.g.list, tuple)
        """
        self.counter = 0
        self.iterator = iter(some_iterable)

    def get_count(self):
        """Returns the current value of the counter"""
        return self.counter

    def __iter__(self):
        return self

    def __next__(self):
        try:
            item = next(self.iterator)
            self.counter += 1
            return item
        except StopIteration:
            raise StopIteration
