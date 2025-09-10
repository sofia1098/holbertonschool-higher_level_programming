#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != None: 
        tupla = (len(sentence), sentence[0])
        return tupla
    else:
        return None