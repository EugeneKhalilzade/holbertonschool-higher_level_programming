#!/usr/bin/env python3
"""extends the Python list class"""


class VerboseList(list):
    """
    extends list to print messages
    """

    def append(self, item):
        """
        append an item to the list with notification.
        """
        super().append(item)
        print(f"Added [{item}] to the list.")

    def extend(self, iterable):
        """
        extend list with items from iterable
        """
        original_length = len(self)
        super().extend(iterable)
        items_added = len(self) - original_length
        print(f"Extended the list with [{items_added}] items.")

    def remove(self, item):
        """
        remove an item from the list
        """
        print(f"Removed [{item}] from the list.")
        super().remove(item)

    def pop(self, index=-1):
        """
        remove and return item at index
        """
        item = self[index]
        print(f"Popped [{item}] from the list.")
        return super().pop(index)
