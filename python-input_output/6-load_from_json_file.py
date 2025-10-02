#!/usr/bin/python3

""" comentario """
import json


def load_from_json_file(filename):
    """ comentario funcion """
    with open(filename) as f:
        return json.load(f)
