#!/usr/bin/python3
"""
Clase de geometria
"""


class BaseGeometry:
    """
    Clase de geometria
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value not isinstance(value, int):
            raise TypeError("<name> must be an integer")
        if value < 0:
            raise ValueError("<name> must be greater than 0")

    class Rectangle(width=0,height=0):
        """
        esta clase es de rectangulos
        """
        def __init__(self, width, height):
            self.__width = width
            self.__height = height

        integer_validator(Rectangle, width)
        integer_validator(Rectangle,height)
