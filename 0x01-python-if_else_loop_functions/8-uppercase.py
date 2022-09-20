#!/usr/bin/python3

def uppercase(str):
    """Prints a string in uppercase followed by a new line

    Args:
        str (string)
    """
    result = ''
    for char in str:
        if ord(char) >= 97 and ord(char) <= 122:
            result += chr(ord(char) - 32)
        else:
            result += char
        print("{:s}".format(result))
