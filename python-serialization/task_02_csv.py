#!/usr/bin/python3
"""convierte de CSV a JSON"""


import csv
import json

def convert_csv_to_json(csv_filename: str):
    """leer csv, guardar en json"""
    try:
        with open(csv_filename, newline= "", encoding="utf-8") as csvfile:
            reader = csv.DictReader(csvfile)
            #Convertir cada fila en diccionario 
            data = list(reader)

        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, indent=4)
        return True

    except FileNotFoundError:
        print(f"Error: File '{csv_filename}' not found.")
        return False

    except Exception as err:
        pprint(f"An error occurred: {err}")
        return False
