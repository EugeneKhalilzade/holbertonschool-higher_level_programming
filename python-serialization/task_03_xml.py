#!/usr/bin/python3
"""
task_03_xml.py serialization and deserialization using
XML as an alternative format to JSON
"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """
    turn python dictionary to xml

    Args:
        dictionary (object): python object
        filename (str): name of the file to write to
    """

    root = ET.Element("data")

    for key, value in dictionary.items():
        child = ET.Element(key)
        child.text = str(value)
        root.append(child)

    tree = ET.ElementTree(root)
    tree.write(filename, encoding='utf-8', xml_declaration=True)

def deserialize_from_xml(filename):
    """
    Read from xml file

    Args:
        filename (str): name of the file to read from

    Returns:
        the data from the xml file as a dictionary
    """

    tree = ET.parse(filename)
    root = tree.getroot()

    data = {}

    for child in root:
        data[child.tag] = child.text

    return data
