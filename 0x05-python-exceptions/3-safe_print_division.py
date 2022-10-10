#!/usr/bin/python3

def safe_print_division(a, b):
    try:
        d = a / b
    except (TypeError, ZeroDivisionError):
        d = None
    finally:
        print("Inside reult: {}".format( d))
    return (d)
