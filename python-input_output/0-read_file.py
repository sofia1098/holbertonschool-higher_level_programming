#!/usr/bin/python3
""" comentario """


def read_file(filename=""):
    """otro comentario """
    with open(filename, enconding="utf-8") as f:
        contenido = f.read()
        print(contenido)
