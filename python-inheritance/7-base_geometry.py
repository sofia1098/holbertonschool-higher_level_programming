#!/usr/bin/python3
"""
clase vacia
"""


class BaseGeometry:
    """
    esta clase esta vacia
    """
    def area(self):
        raise Exception("area() is not implemented")

    def integer_validator(self, name, value):
        if value is not isinstance(value, int):
            raise TypeError("name must be an integer")
        if value < 0:
            raise ValueError("name must be greater than 0")
