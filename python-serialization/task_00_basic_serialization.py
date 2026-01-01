#!/usr/bin/python3
"""
task_00_basic_serialization.py module that serializes a python
dictionary to a JSON file and deserializes the JSON file to
recreate the python dictionary
"""
import json


def serialize_and_save_to_file(data, filename):
    """
    serializes data and saves it to a file

    Args:
        data (object): python object
        filename (str): name of file to save the serialized data
    """

    with open(filename, "w") as file:
        json.dump(data, file)


def load_and_deserialize(filename):
    """
    loads and deserializes data from a specified file

    Args:
        filename (str): name of the file to load data from

    Returns:
        returns a python object with the deserialized JSON data
    """

    with open(filename, "r") as file:
        return json.load(file)
