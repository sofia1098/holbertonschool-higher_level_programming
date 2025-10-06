#!/usr/bin/python3
""" XML files"""


import xml.etree.cElementTree as ET


def serialize_to_xml(dictionary: dict, filename: str):
    """De diccionario a XML file"""
    try:
        root = ET.Element("data")
        for key, value in dictionary.items():
            child = ET.SubElement(root, key)
            child.text = str(value)
        
        tree = ET.ElementTree(root)
        tree.write(filename, encoding="utf-8", xml_declaration=True)

    except Exception as e:
        print(f"Serialization failed: {e}")

def deserialize_from_xml(filename: str)
    """de XML a diccionario"""
    try:
        tree = ET.parse(filename)
        root = tree.getroot()

        result = {}
        for child in root:
            result[child.tag] = child.text
        return result

    except Exception as e:
        print(f"Deserialization failed: {e}")
        return {}
