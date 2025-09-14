#!/usr/bin/python3
"""
This function ands rwo integres
"""
def add_integer(a, b=98):
 """
    Adds two integers.

        a: The first number (int or float).
        b: The second number (int or float).

    Returns: Sum of a and b.
"""
    if not isinstance(a, (int, float)):
        raise TypeError("a must be an integer")
    if not isinstance(b, (int, float)):
        raise TypeError("b must be an integer")

    return int(a) + int(b)
