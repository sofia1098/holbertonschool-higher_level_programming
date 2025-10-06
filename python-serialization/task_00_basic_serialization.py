#!/usr/bin/python3
""" Convierte un diccionario a JSON 
y viceversa loads dumps"""


import json


def serialize_and_save_to_file(data, filename):
    """dicccionario a json """
    with open(filename, 'w') as f:
        json.dump(data, f, indent=4)

def load_and_deserialize(filename):
    """De json a diccionario"""
    with open(filename) as f:
        return json.load(f)
