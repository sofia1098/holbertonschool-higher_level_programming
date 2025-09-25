#!/usr/bin/python3
"""
Clase de geometria
"""
BaseGeometry = __import__('7-base_geometry').BaseGeometry


class Rectangle(width=0,height=0):
    """
    esta clase es de rectangulos
    """
    def __init__(self, width, height):
        self.integer_validator("width", width)
        self.__width = width
        self.integer_validator("height", height)
        self.__height = height
