#!/usr/bin/python3
""" comentario"""

class CountedIterator:

    def __init__(self, iterable):
        self.iterator = iter(iterable) #iterador interno
        self.count = 0 #contador de elementos

    def __iter__(self):
        return self

    def __netx__(self):
        item = next(self.iterator)
        self.count += 1
        return item

    def get_count(self):
        return self.count
