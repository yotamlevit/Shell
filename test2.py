# -*- coding: utf-8 -*-
import subprocess
import sys

def main():
    """
    Add Documentation here
    """
    print subprocess.check_output(['python', 'F:/GitHub/Shell/HexDump.py', 'bin.txt'])
    """
    pip_data = subprocess.check_output(['C:/Windows/System32/systeminfo.exe'])
    with open('in_out.txt', 'w') as pipe:
        pipe.write(pip_data)
    file_obj = open('in_out.txt', "r")
    #print file_obj
    print subprocess.check_output(['python', 'F:/GitHub/Shell/HexDump.py'], stdin=file_obj)
    pip_data = subprocess.check_output(['C:/Windows/System32/systeminfo.exe'])
    print pip_data
    with open('in_out.txt', 'w') as pipe:
        pipe.write(pip_data)###############need to fox the subprocess.PIPE
    with open('in_out.txt', 'r') as pipe:
        subprocess.PIPE = pipe.read()
    subprocess.PIPE = pipe
    print subprocess.PIPE
    print subprocess.check_output(['python', 'F:/GitHub/Shell/HexDump.py'], stdin=pip_data)
    print "############################################################"
    print ["C:/Windows/System32/where.exe"] + ["notepad"]
    print subprocess.check_output(["C:/Windows/System32/where.exe"] + ["notepad"])
    #print subprocess.check_output("ipconfig /renew" ).decode('utf-8')

"""
if __name__ == '__main__':
    main()