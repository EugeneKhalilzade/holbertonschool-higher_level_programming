#!/usr/bin/env python3
"""Abstract Base Classes (ABCs)"""
from abc import ABC, abstractmethod
import math


class Shape(ABC):
    """
    for calculating area and perimeter
    """

    @abstractmethod
    def area(self):
        """
        calculate and return the area
        """
        pass

    @abstractmethod
    def perimeter(self):
        """
        calculate and return the perimeter
        """
        pass


class Circle(Shape):
    """
    circle with a given radius and implements
    """

    def __init__(self, radius):
        """
        initialize the circle with given radius.
        """
        self.radius = abs(radius)

    def area(self):
        """
        calculate the area of the circle.
        """
        return math.pi * self.radius ** 2

    def perimeter(self):
        """
        calculate the perimeter
        """
        return 2 * math.pi * self.radius


class Rectangle(Shape):
    """
    a rectangle with given width and height
    """

    def __init__(self, width, height):
        """
        initialize the rectangle
        """
        self.width = width
        self.height = height

    def area(self):
        """
        calculate the area of the rectangle
        """
        return self.width * self.height

    def perimeter(self):
        """
        calculate the perimeter
        """
        return 2 * (self.width + self.height)


def shape_info(shape):
    """
    print area and perimeter
    """
    print(f"Area: {shape.area()}")
    print(f"Perimeter: {shape.perimeter()}")
