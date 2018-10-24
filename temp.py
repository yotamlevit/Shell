import os
import binascii

FILE_PATH = "C:/Users/cyber/Documents/GitHub/shell/bin.txt"

def is_file(path):
    return os.path.isfile(path)

def converter(text):
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
    Add Documentation here
    """
    if is_file(FILE_PATH):
        with open(FILE_PATH, 'rb') as r:
            text = r.read()
        print(converter(text))

if __name__ == '__main__':
    main()