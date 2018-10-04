# -*- coding: utf-8 -*-
import getpass
import os

PATH_TO_TOOl = "C:/Users/cyber/PycharmProjects/shell"

def is_file(tool):
    print PATH_TO_TOOl + "/" + tool + ".py"
    return os.path.isfile(PATH_TO_TOOl + "/" + tool + ".py")


def main():
    done = False
    print "Hello, " + getpass.getuser()
    while not done:
        input_ = raw_input("")
        if input_ == "exit":
            done = True
        if is_file(input_):
            print PATH_TO_TOOl + "/" + input_ + ".py"
            os.system(PATH_TO_TOOl + "/" + input_ + ".py")

if __name__ == '__main__':
    main()