#!/usr/bin/python3

def delete_at(my_list=[], idx=0):
    for x in my_list:
        del my_list[idx]
        return (my_list)
    if idx < 0 or idx >= (len(my_list)):
        return None
