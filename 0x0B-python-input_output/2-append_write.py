#!/usr/bin/python3
"""Define a function that appends a string to a text file"""


def write_file(filename="", text=""):
    """Function appends a string to a text file"""
    with open(filename, "a", encoding="utf-8") as f:
        return f.write(text)
