#!/usr/bin/python3

def print_matrix_integer(matrix=[[]]):
    for row in matrix:
        for i in row[:-1]:
            print("{:d} ".format(i), end="")
        if row:
            print("{:d}".format(row[-1]))
