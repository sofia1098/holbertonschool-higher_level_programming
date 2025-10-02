#!/usr/bin/python3
""" comentario """


def append_write(filename="", text=""):
    """comentario fun:cion"""
    with open(filename, "a", encoding="utf-8") as f:
        f.write(text)
        return len(text)
