#!/usr/bin/python3

"""hola hola"""
Rectangle = __import__('9-rectangle').Rectangle


class Square(Rectangle):
    """ clase de cuadrado"""
    def __init__(self, size):
        self.integer_validator("size", size)
        super().__init__(size, size)
        self.__size = size

    def area(self):
        return (self.__size ** 2)

    def __str__(self):
        return "[Square] {}/{}".format(self.__size, self.__size)
