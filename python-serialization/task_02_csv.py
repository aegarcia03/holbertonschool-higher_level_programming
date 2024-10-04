#!/usr/bin/env python3
"""This module reads data from CSV and writes the JSON data to a file"""
import json
import csv


def convert_csv_to_json(csv_filename):
    json_file = 'data.json'
    data = []
    try:
        with open(csv_filename, 'r', encoding="UTF8") as cvsf:
            csv_reader = csv.DictReader(cvsf)
            for row in csv_reader:
                data.append(row)
    except FileNotFoundError:
        return False

    try:
        with open(json_file, 'w', encoding="UTF8") as jsonf:
            json.dump(data, jsonf, indent=4)
        return True
    except:
        return False
