#!/usr/bin/python3

def print_last_digit(number):
    if number < 0 or number % 10 == number:
        number = ((-1) * number) % 10
    print("{:d}".format(number), ends="")
    return number
