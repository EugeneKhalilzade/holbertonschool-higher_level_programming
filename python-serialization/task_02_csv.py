#!/usr/bin/python3
"""
task_02_csv.py reading data from one format (CSV) and
converting it into another format (JSON)
"""
import csv
import json


def convert_csv_to_json(csv_file):
    """
    convert csv to json

    Args:
        csv_file (str): name of the csv file

    Returns:
        bool: True if conversion was successful, False otherwise
    """

    data = []

    try:
        with open(csv_file, encoding="utf-8") as csvfile:
            csv_read = csv.DictReader(csvfile)
            for row in csv_read:
                data.append(row)

    except FileNotFoundError:
        return False

    try:
        with open("data.json", "w", encoding="utf-8") as jsonfile:
            json.dump(data, jsonfile, ensure_ascii=False, indent=4)
    except:
        return False
    return True
