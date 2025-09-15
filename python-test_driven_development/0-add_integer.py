#!/usr/bin/python3
"""
This module contains a function that adds two integers
"""

def add_integer(a, b=98):
    """
    Adds two integers.

    a: The first number (int or float)
    b: The second number (int or float, default is 98)

    Returns: Sum of a and b as an integer
    Raises:
        TypeError: if a or b is not an int or float
    """
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")

    return int(a) + int(b)
