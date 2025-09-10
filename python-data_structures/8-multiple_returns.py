#!/usr/bin/python3
def multiple_returns(sentence):
    if sentence != "": 
        tupla = (len(sentence), sentence[0])
        return tupla
    else:
        return (0, None)