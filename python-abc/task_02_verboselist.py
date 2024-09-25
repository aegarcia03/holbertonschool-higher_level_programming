#!/usr/bin/env python3


class VerboseList(list):
    """A VerboseList class that inherits from the built-in `list` class"""

    def append(self, item):
        """Appends a new item
        Args:
            item: item to be added to the list
        Returns:
            A list with the new item added
        """
        super().append(item)
        print(f"Added [{item}] to the list")

    def extend(self, items):
        """Extends the list
        Args:
            items: the iterable of items to add to the list
        """
        super().extend(items)
        print(f"Extended the list with [{len(items)}] items")

    def remove(self, item):
        """Removes an item from the list
        Args:
            item: item to be removed
        Return:
            list with removed item
        """
        super().remove(item)
        print(f"Removed [{item}] from the list")

    def pop(self, idx=-1):
        """Removes an item at the specified positon
        Args:
            item: item to be removed
            idx: position
        Return:
            list with removed item
            if last item is not specified, pop the last item
        """
        item = super().pop(idx)
        print(f"Popped [{item}] from the list")
        return item
