#!/usr/bin/env python3
"""Defines a module that adds"""
import pickle


def serialize_and_save_to_file(data, filename):
    with open(filename, mode="wb") as file:
        pickle.dump(data, file)


def load_and_deserialize(filename):
    with open(filename, mode="rb") as file:
        return pickle.load(file)
