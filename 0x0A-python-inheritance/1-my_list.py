#!/usr/bin/python3
"""Inherits from list"""


class MyList(list):
    """super class"""
    def print_sorted(self):
        """sorts a list"""
        print(sorted(self))
