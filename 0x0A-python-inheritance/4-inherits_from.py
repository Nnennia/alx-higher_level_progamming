#!/usr/bin/python3
"""Checks object inheritance"""


def inherits_from(obj, a_class):
    """Checks if an object is a subclass"""
    if issubclass(type(obj), a_class):
        if type(obj) != a_class:
            return True
    return False
