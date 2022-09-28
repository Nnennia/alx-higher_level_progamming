#!/usr/bin/python3

def search_replace(my_list, search, replace):
    """Replaces all occurance of any element by another in a new list

    Args:
        my_list : initial list
        search : element to replace in the list
        replace : new element
    """

    for x in range(len(my_list)):
        if my_list[x] == search:
            my_list[x] = replace
            return my_list
