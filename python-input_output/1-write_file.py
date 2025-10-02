#!/usr/bin/python3
""" comentario """


def write_file(filename="", text=""):
    """comentario de funcion"""
    with open(filename, "w", encoding="utf-8") as f:
        return f.write(text)
