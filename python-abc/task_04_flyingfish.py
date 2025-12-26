#!/usr/bin/env python3
"""inherits from both a Fish class and a Bird class"""


class Fish:
    """
    fish class with swimming and habitat methods
    """

    def swim(self):
        """
        print
        """
        print("The fish is swimming")

    def habitat(self):
        """
        print
        """
        print("The fish lives in water")


class Bird:
    """
    bird class with flying and habitat methods
    """

    def fly(self):
        """
        print
        """
        print("The bird is flying")

    def habitat(self):
        """
        print
        """
        print("The bird lives in the sky")


class FlyingFish(Fish, Bird):
    """
    flyingFish class inheriting from both Fish and Bird
    """

    def swim(self):
        """
        print
        """
        print("The flying fish is swimming!")

    def fly(self):
        """
        print
        """
        print("The flying fish is soaring!")

    def habitat(self):
        """
        print
        """
        print("The flying fish lives both in water and the sky!")
