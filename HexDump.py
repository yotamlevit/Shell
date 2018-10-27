"""
date: 25/10/2018
Name: shell project
Yotam Levit
"""
import os
import binascii
import sys


def is_file(path):
    """
    check is file and or his path exist
    ;path: the path that is checked
    return: True if exist
            False if not exist
    """
    return os.path.isfile(path)


def converter(text):
    """
    convert a regular text to hex
    ;text: the text that is wanted to
           be converted
    return: the hex value of text
    """
    hex_text = binascii.hexlify(text)
    count = 0
    hex_ret = ""
    for char in hex_text:
        count += 1
        if count == 2:
            hex_ret += str(char) + ":"
            count = 0
        else:
            hex_ret += str(char)
    return hex_ret


def main():
    """
    the main function, check if there
    is value in sys.argv and if do so convert
    to hex the file in the path. else
    will convert the input from the stdin
    """
    if len(sys.argv) > 1:
        if is_file(sys.argv[1]):
            with open(sys.argv[1], 'rb') as r:
                text = r.read()
            print(converter(text))
        else:
            print converter(sys.argv[1])
    elif sys.stdin is not None:
        text = ""
        for line in sys.stdin:
            text += line
        print(converter(text))
    else:
        print "Invalid piping"
if __name__ == '__main__':
    main()