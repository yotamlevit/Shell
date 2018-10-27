# -*- coding: utf-8 -*-
"""
date: 25/10/2018
Name: shell project
Yotam Levit
"""
import sys

HELLO = "Hello world "


def main():
    """
    the main function, check if there
    is value in sys.argv and if do so add it to the
    output. check if there is an stdin input, if there
    is an input so add it to the output. other otherwise
    the output will be only Hello World
    """
    if len(sys.argv) > 1:
        print(HELLO + sys.argv[1])
    elif sys.stdin is not None:
        text = ""
        for line in sys.stdin:
            text += line
        print(HELLO + text)
    else:
        print(HELLO)
if __name__ == '__main__':
    main()