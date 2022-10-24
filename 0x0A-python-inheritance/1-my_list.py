#!/usr/bin/python3
""" A class """


from types import prepare_class


class MyList(list):
    """ Inherits the list class """
    pass

    def print_sorted(self):
        """Sorts a list"""
        print(sorted(self))
