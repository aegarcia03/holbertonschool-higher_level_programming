#!/usr/bin/env python3
"""This module defines serialization and deserialization using XML"""
import xml.etree.ElementTree as ET


def serialize_to_xml(dictionary, filename):
    """Serializes the a Python dictionary into XML"""
    root = ET.Element('data')
    for key, value in dictionary.items():
        child = ET.SubElement(root, key)
        child.text = str(value)

    tree = ET.ElementTree(root)
    tree.write(filename)


def deserialize_from_xml(filename):
    """Returns a deserialized Python dictionary from a XML file"""
    tree = ET.parse(filename)
    root = tree.getroot()

    dictionary = {}
    for child in root:
        dictionary[child.tag] = child.text

    return dictionary
