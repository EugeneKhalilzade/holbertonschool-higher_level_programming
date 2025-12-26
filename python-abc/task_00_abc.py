#!/usr/bin/env python3
"""Abstract Base Classes (ABCs)"""
from abc import ABC, abstractmethod


class Animal(ABC):
    """
    Animal class, ensuring it inherits from ABC
    """

    @abstractmethod
    def sound(self):
        """
        return the sound the animal makes.
        """
        pass


class Dog(Animal):
    """
    inherits from the Animal class
    """

    def sound(self):
        """
        to return the string "Bark"
        """
        return "Bark"


class Cat(Animal):
    """
    inherits from the Animal class
    """

    def sound(self):
        """
        to return the string "Meow"
        """
        return "Meow"
