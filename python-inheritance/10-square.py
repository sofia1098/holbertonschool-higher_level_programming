#!/usr/bin/python3
Square = __import__(9-rectangle.py).Rectangle
"""un cuadrado """


class Square(Rectangle):
    """ clase de cuadrado"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
