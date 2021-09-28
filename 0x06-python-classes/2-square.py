#!/usr/bin/python3
""" Module 2-squares.py """
class Square:
    """Represents a square.
    Private Instance attribute: size.
    Instantiation with optional size.
    """

    def __init__(self, size=0):
        """Initializes the data."""
        if not isinstance(size, int):
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("aize must be >= 0")
        self.__size = size
