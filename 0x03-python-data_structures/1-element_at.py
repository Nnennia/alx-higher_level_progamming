#!/usr/bin/python3

def element(my_list, idx):
    for idx in my_list:
        if idx < 0 and idx > (len(my_list - 1)):
            return None
        return my_list[idx]
