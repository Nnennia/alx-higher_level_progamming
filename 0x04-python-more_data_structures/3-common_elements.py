#!/usr/bin/python3

def common_elements(set_1, set_2):
    """Returns a set of commmon elements in two sets

    Args:
        set_1 (set): set to check
        set_2 (set): set to check
    """
    if len(set_1.intersection(set_2)) > 0:
        return (set_1.intersection(set_2))
