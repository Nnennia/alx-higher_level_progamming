#!/usr/bin/python3
"""find an object insatnce"""


def is_kind_of_class(obj, a_class):
    """Instance of a class"""
    if isinstance(obj, a_class):
        return True
    return False
