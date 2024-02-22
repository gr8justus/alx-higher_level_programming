#!/usr/bin/python3
"""
    This module contains class square
"""


class Square:
    """
        This class defines a square

        Args:
            size: the size of square

        Attributes:
            size: the size of square
    """

    def __init__(self, size=0):
        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size

    def area(self):
        """
            Calculates the area of a square
        """

        return self.__size ** 2
