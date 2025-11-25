#!/usr/bin/python3

def islower(c):
    if not isinstance(c, str) or len(c) != 1:
        raise TypeError("c must be a single character string")

    return c.islower()

islower = __import__('7-islower').islower
