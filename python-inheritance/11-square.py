#!/usr/bin/python3
"""class Square that inherits from Rectangle"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """
    Instantiation with size
    """

    def __init__(self, size):
        """
        size must be private. No getter or setter
        size must be a positive integer,
        validated by integer_validator
        """
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def __str__(self):
        """
        return, the square description
        """
        return f"[Square] {self.__size}/{self.__size}"
