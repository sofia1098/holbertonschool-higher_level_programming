#!/usr/bin/python3
"""
Function matrix_divided that divides all
elements of a matrix by a given number
"""

def matrix_divided(matrix, div):
    """
    Divides all elements of a matrix by div and returns a new matrix

    matrix: A list of lists of integers/floats
    div: The divisor (int or float)

    Return: A new matrix with each element divided
    """
    for row in matrix:
        if not isinstance(row, list):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")
    for num in row:
        if not isinstance(num, (int, float)):
            raise TypeError("matrix must be a matrix (list of lists) of integers/floats")

    if len(matrix) > 0:
        row_length = len(matrix[0])
        for row in matrix:
            if len(row) != row_length:
                raise TypeError("Each row of the matrix must have the same size")

    if not isinstance(div, (int, float)):
        raise TypeError("div must be a number")

    if div == 0:
        raise ZeroDivisionError("division by zero")

    new_matrix = []
    for row in matrix:
        new_row = []
        for num in row:
            new_row.append(round(num / div, 2))
        new_matrix.append(new_row)

    return new_matrix
