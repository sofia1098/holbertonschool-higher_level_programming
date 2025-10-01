#!/usr/bin/python3
import os
""" comentario """


def read_file(filename=""):
    with open(filename, enconding="utf-8") as f:
    contenido = f.read()
    print(contenido)
