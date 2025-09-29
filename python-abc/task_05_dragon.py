#!/usr/bin/python3
""" comentario"""

class SwimMixin:

    def swim(self):
        print("The crature swims!")

class FlyMixin:
    def fly(self):
        print("The creature flies!")

class Dragon(SwimMixin, FlyMixin):

    def roar(self)
        print("The dragon roars!")
