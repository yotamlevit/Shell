# -*- coding: utf-8 -*-
import getpass
import os

PATH_TO_TOOl = "C:/Windows/System32;C:/Users/ben-horin/Desktop/Shell"


def detect_file(tool, path):
    temp = path.split("/")
    if temp[len(temp)-1] == "Shell":
        return path + "/" + tool + ".py"
    else:
        return path + "/" + tool + ".exe"

def is_file(tool, path):
    return os.path.isfile(detect_file(tool, path))


def main():
    done = False
    did_it = False
    print "Hello, " + getpass.getuser()
    while not done:
        input_ = raw_input("Enter your command: ")
        if input_ == "exit":
            done = True
        for path in PATH_TO_TOOl.split(";"):
            print path
            if did_it:
                break
            if is_file(input_, path):
                print "a"
                os.system(detect_file(input_, path))
                did_it = True
        did_it = False

if __name__ == '__main__':
    main()