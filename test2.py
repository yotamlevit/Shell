# -*- coding: utf-8 -*-
import subprocess
import sys

def main():
    """
    Add Documentation here
    """
    print ["C:/Windows/System32/where.exe"] + ["notepad"]
    print subprocess.check_output(["C:/Windows/System32/where.exe"] + ["notepad"])
    #print subprocess.check_output("ipconfig /renew" ).decode('utf-8')


if __name__ == '__main__':
    main()