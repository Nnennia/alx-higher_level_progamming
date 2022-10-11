#!/usr/bin/python3
"""define the area of the sqaure"""


class Square:
    """Square"""
    def __init__(self, size=0):
        if not isinstance(size, int):
            raise TypeError("size mut be an integer")
        elif size < 0:
            raise ValueError("size must be >= 0")

    def area(self):
        return (self.__size * self.__size)
