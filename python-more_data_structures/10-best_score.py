#!/usr/bin/python3
def best_score(a_dictionary):
    if not a_dictionary:
        return None
    max_key = 0
    max_value = 0
    for key, value in a_dictionary.tems():
        if value > max_value:
            max_value, max_key = value, key
    return max_key
