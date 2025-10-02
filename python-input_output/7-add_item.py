#!/usr/bin/python3

""" comentario """
import sys
import os
save_to_json_file = __import__('5-save_to_json_file').save_to_json_file
load_from_json_file = __import__('6-load_from_json_file').load_from_json_file

if __name__ == '__main__':
    try:
        data = load_from_json_file(filename)
    except Exception:
        data = []

    #if not isinstance(data, list):
        #data = [data]

    data.extend(sys.argv[1:])
    save_to_json_file(data, filename)
