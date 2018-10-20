# -*- coding: utf-8 -*-
import subprocess

def main():
    """
    Add Documentation here
    """
    proc = subprocess.Popen(['cdrecord', '--help'], stderr=subprocess.PIPE)
    output = proc.stderr.read()
    print output



if __name__ == '__main__':
    main()