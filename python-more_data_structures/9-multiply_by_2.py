#!/usr/bin/python3
def multiply_by_2(a_dictionary):
    new = {}
    for key, i in a_dictionary.items():
        new[key] = i * 2
    return new
