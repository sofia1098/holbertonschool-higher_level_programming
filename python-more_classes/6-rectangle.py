#!/usr/bin/python3
"""Clase Rectangulo"""


class Rectangle:
    """clase rectangulo"""
    number_of_instances = 0

    def __init__(self, width=0, height=0):
        self.width = width
        self.height = height
        Rectangle.number_of_instances += 1

    @property
    def width(self):
        return self.__width

    @property
    def height(self):
        return self.__height

    @width.setter
    def width(self, value):
        if not isinstance(value, int):
            raise TypeError("width must be an integer")
        if value < 0:
            raise ValueError("width must be >= 0")
        self.__width = value

    @height.setter
    def height(self, value):
        if not isinstance(value, int):
            raise TypeError("height must be an integer")
        if value < 0:
            raise ValueError("height must be >= 0")
        self.__height = value

    def area(self):
        return self.__width * self.__height

    def perimeter(self):
        if self.__width == 0 or self.__height == 0:
            return 0
        else:
            return ((self.__height * 2) + (self.__width * 2))

    def my_print(self):
        if self.__width == 0 or self.__height == 0:
            print("")
        else:
            for i in range(self.__height):
                for j in range(self.__width):
                    print("#", end="")
                print()

    def __str__(self):
        if self.width == 0 or self.height == 0:
            return ""
        result = ""
        for i in range(self.height):
            result += "#" * self.width
            if i != self.height - 1:
                result += "\n"
        return result

    def __repr__(self):
        return "Rectangle({}, {})".format(self.width, self.height)

    def __del__(self):
        Rectangle.number_of_instances -= 1
        print("Bye rectangle...")
