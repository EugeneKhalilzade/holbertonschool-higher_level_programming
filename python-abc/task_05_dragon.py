#!/usr/bin/env python3
"""two mixin classes, SwimMixin and FlyMixin"""


class SwimMixin:
    """
    with a method swim that print
    """

    def swim(self):
        """
        print
        """
        print("The creature swims!")


class FlyMixin:
    """
    with a method fly that print
    """

    def fly(self):
        """
        print
        """
        print("The creature flies!")


class Dragon(SwimMixin, FlyMixin):
    """
    inherits from both SwimMixin and FlyMixin
    """

    def roar(self):
        """
        print
        """
        print("The dragon roars!")
