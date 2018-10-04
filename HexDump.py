import os
import sys

FILE_PATH = "C:/Users/cyber/PycharmProjects/shell/bin.txt"

def is_file(path):
    return os.path.isfile(path)

def conv_to_hex(text):
    hex_text = ':'.join([x.encode('hex') for x in text])
    return hex_text

def main():
    """
    Add Documentation here
    """

    with open(FILE_PATH, 'rb') as r:
        text = r.read()
    print(conv_to_hex(text))

if __name__ == '__main__':
    main()