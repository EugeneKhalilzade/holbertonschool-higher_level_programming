#!/usr/bin/python3
"""Module for LockedClass"""


class LockedClass:
    """Class that only allows the first_name attribute"""
    __slots__ = ("first_name",)
