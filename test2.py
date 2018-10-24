# -*- coding: utf-8 -*-
import subprocess

def main():
    """
    Add Documentation here
    """
    input1 = "HexDump | bin.txt"
    temp = input1.split("|")
    action = []
    for t in temp:
        s = t.lstrip(" ")
        s = s.split(" ")
        print s
        if s[0] != " ":
            action.append(s[0])
    print action


if __name__ == '__main__':
    main()