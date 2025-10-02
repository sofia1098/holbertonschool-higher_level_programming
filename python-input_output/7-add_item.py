#!/usr/bin/python3

""" comentario """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    filename = "add_item.json"
    if os.path.exists("./add_item.json"):
        lista = list(load_from_json_file(filename))
    else:
        my_list = []

    lista.extend(sys.argv[1:])
    save_to_json_file(lista, filename)
