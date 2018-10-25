# -*- coding: utf-8 -*-
import sys

def main():
    """
    Add Documentation here
    """
    if len(sys.argv) > 1:
        print("Hello world" + sys.argv[1])
    else:
        print("Hello to the world")


if __name__ == '__main__':
    main()