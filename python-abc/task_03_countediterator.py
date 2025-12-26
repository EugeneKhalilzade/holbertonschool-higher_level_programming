#!/usr/bin/env python3
"""extends the built-in iterator obtained from the iter function"""


class CountedIterator:
    """
    keep track of the number of items that have been iterated over
    """

    def __init__(self, iterable):
        """
        initialize CountedIterator with an iterable.
        """
        self.iterator = iter(iterable)
        self.count = 0

    def __next__(self):
        """
        fetch next item
        """
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        """
        return the current count of iterated items
        """
        return self.count
