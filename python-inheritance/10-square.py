#!/usr/bin/python3
"""un cuadrado """
Rectangle = __import__(9-rectangle.py).Rectangle


class Square(Rectangle):
    """ clase de cuadrado"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size
