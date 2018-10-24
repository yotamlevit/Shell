# -*- coding: utf-8 -*-
import getpass
import os
import sys
import subprocess

path_to_tool = sys.argv[0].split("/")
path_to_tool.pop()
temp = ""
for word in path_to_tool:
    temp += word + "/"
path_to_tool = temp[:-1]

PATH_TO_TOOL = "C:/Windows/System32" + ";" + path_to_tool


def detect_file(tool, path):
    temp = path.split("/")
    if temp[len(temp)-1] == "Shell":
        return path + "/" + tool + ".py"
    else:
        return path + "/" + tool + ".exe"


def is_file(tool, path):
    return os.path.isfile(detect_file(tool, path))


def find_and_run(input1):
    did_it = False
    temp = input1.split("|")
    action = []
    for t in temp:
        s = t.lstrip(" ")
        s = s.split(" ")
        print s
        if s[0] != " ":
            action.append(s[0])
    for path in PATH_TO_TOOL.split(";"):
            if did_it:
                break
            if is_file(action[0], path):
                if len(action) < 2:
                    ######     need to do an empty תא for the ipconfig
                    print action
                value = ["python", detect_file(action[0], path)] + [action[1]]
                print subprocess.check_output(value)
                #os.system(detect_file(input1, path))
                did_it = True


def main():
    done = False
    print "Hello, " + getpass.getuser()
    while not done:
        input_ = raw_input("Enter your command: ")
        if input_ == "exit":
            done = True
        find_and_run(input_)

if __name__ == '__main__':
    main()