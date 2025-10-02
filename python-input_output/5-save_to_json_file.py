#!/usr/bin/python3

""" comentario """
import json

def save_to_json_file(my_obj, filename):
    """ comentario funcion """
    open(filename, "w", encoding="utf-8") as f:
        f.write(json.dumps(my_obj))
