#!/usr/bin/python3
"""Coordinates of a square"""


class Square:
    """defines a square"""
    def __init__(self, size=0, position=(0, 0)):
        """Initialize a new square"""
        self.size = size
        self.position = position

    @property
    def size(self):
        """Size"""
        return (self.__size)

    @property
    def position(self):
        """Position"""
        return (self.__poition)

    @size.setter
    def size(self, value):
        """size"""
        if not isinstance(value, int):
            raise TypeError("size must be an integer")
        elif value < 0:
            raise ValueError("size must be >= 0")
        self.__size = value

    @position.setter
    def position(self, value):
        """position"""
        if (not isinstance(value, tuple) or len(value) != 2 or
            not all(isinstance(num, int) for num in value) or not
                all(num >= 0 for num in value)):
            raise TypeError("position must be a tuple of 2 positive integers")
        self.__position = value

    def area(self):
        """area"""
        return (self.__size * self.__size)

    def my_print(self):
        """Print the square with the # character."""
        if self.__size == 0:
            print("")
            return

        [print("") for x in range(0, self.__position[1])]
        for x in range(0, self.__size):
            [print(" ", end="") for y in range(0, self.__position[0])]
            [print("#", end="") for n in range(0, self.__size)]
            print("")
