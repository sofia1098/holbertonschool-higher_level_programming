#!/usr/bin/python3
from abc import ABC, abstractmethod
""" comentario"""


class Animal(ABC):
    """Clase abstracta"""

    @abstractmethod
    def sound(self):
        pass

class Dog(Animal):
    def sound(self):
        return "Bark"

class Cat(Animal):
    def sound(self):
        return "Meow"
