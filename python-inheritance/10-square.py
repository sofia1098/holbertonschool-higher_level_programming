#!/usr/bin/python3
from 9-rectangle.py import Rectangle
"""un cuadrado """


class Square(Rectangle):
    """ clase de cuadrado"""
    def __init__(self, size):
        self.integer_validator("size", size)
        self.__size = size
