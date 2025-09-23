#!/usr/bin/python3
"""
This module defines a function that checks if an object
is exactly an instance of a specified class
"""


def is_same_class(obj, a_class):
    """
    Returns True if obj is exactly an instance of a_class,
    otherwise False.

    Args:
        obj: object to check
        a_class: class to compare with

    Returns:
        bool: True if obj is exactly an instance of a_class
    """
    return type(obj) is a_class
