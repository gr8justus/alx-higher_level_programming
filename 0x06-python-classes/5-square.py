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
        self.size = size

    def area(self):
        """
            Calculates the area of a square
        """

        return self.__size ** 2

    def my_print(self):
        """
            Prints the square to stdout
        """

        if self.size == 0:
            print()
        else:
            for length in range(self.size):
                for width in range(self.size):
                    print("#", end="")
                print()

    @property
    def size(self):
        """
            Retrieves the value of size
        """

        return self.__size

    @size.setter
    def size(self, size):
        """
            sets the value of size
        """

        if isinstance(size, int) is False:
            raise TypeError("size must be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")
        else:
            self.__size = size
