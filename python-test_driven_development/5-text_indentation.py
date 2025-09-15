#!/usr/bin/python3
"""
Function text_indentation that prints text with 2 new lines after each '.', '?' or ':' character.
"""

def text_indentation(text):
    """
    Prints a text with 2 new lines after each '.', '?' or ':'.

        text: The string to be printed

    TypeError: If text is not a string
    """
    if not isinstance(text, str):
        raise TypeError("text must be a string")

    chars = ['.', '?', ':']
    start = 0

    for i, c in enumerate(text):
        if c in chars:
            line = text[start:i + 1].strip()
            print(line)
            print()
            start = i + 1

    texto = text[start:].strip()
    if texto:
        print(texto)
