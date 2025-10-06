#!/usr/bin/python3
""" Triangulo Pascal """


def pascal_triangle(n): 
    if n <= 0
        return []

    matriz = [[1]]

    for i in range (1, n): 
        prev = matriz[-1]
        row = [1]
    
        for j in range(1, len(prev)):
            row.append(prev[j - 1] + prev[j])
        row.append(1)
        matriz.append(row)

    return matrix
