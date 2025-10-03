#!/usr/bin/python3
""" Module that defines Student class """


class Student:
    """ comentario """
    def __init__(self, first_name, last_name, age):
        self.first_name = first_name
        self.last_name = last_name
        self.age = age

    def to_json(self, attrs=None):
        if isinstance(attrs, list) and all(isinstance(x, str) for x in attrs):
            """comprension de diccionario, k se guarda temp.
             devuelve los atri que esten en la lista y en el obj"""
            return {k: self.__dict__[k] for k in attrs if k in self.__dict__}
        return self.__dict__
