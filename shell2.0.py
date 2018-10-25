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
        return [path + "/" + tool + ".py", "python"]
    else:
        return [path + "/" + tool + ".exe", "exe"]

def find_path(action):
        did_it = False
        found = "None"
        for path in PATH_TO_TOOL.split(";"):
            if did_it:
                break
            if is_file(action, path):
                found = path
                did_it = True
        return found

def is_file(tool, path):
    return os.path.isfile(detect_file(tool, path)[0])

def get_action(user_input):
    temp = user_input.split("|")
    action = []
    for t in temp:
        s = t.lstrip(" ")
        s = s.split(" ")
        if s[0] != " ":
            action.append(s[0])
            if len(s) > 1 and s[1] != "":
                temp1 = action.pop()
                action.append("space")
                action.append(temp1)
                action.append(s[1])
    return action

def find_and_run(input1):
    action = get_action(input1)
    x = len(action)
    i = 0
    text1 = False
    space = False
    std = False
    pip_data = ""
    while i < x:
        if std:
            path = find_path(action[i])
            if path != "None":
                file_info = detect_file(action[i], path)
                if file_info[1] == "python":
                    if pip_data != "":
                        value = [file_info[1], file_info[0]] + [pip_data]
                else:
                    value = [file_info[0]] + [pip_data]
                    std = True
                pip_data = subprocess.check_output(value, stdin=subprocess.Pi)###########need to fix subprocces.PIPE
        elif space:
            path = find_path(action[i])
            if path != "None":
                file_info = detect_file(action[i], path)
                value = [file_info[0]] + [action[i+1]]
                i += 2
                space = False
                try:
                    pip_data = subprocess.check_output(value)
                    if i == x:
                        print pip_data
                except:
                    print "Error: failed open a pipe"
                    print "Error > ",sys.exc_info()[0]
            else:
                print action[i] + " is not recognized as an internal command"
                break
        elif action[i] == "space":
            space = True
            i += 1
        elif ".txt" in action[i]:
            pip_data = action[i]
            if text1:
                print "invalid pip"
                break
            text1 = True
            i += 1
        else:
            path = find_path(action[i])
            if path != "None":
                file_info = detect_file(action[i], path)
                if file_info[1] == "python":
                    if pip_data != "":
                        value = [file_info[1], file_info[0]] + [pip_data]
                    else:
                        value = [file_info[1], file_info[0]]
                else:
                    value = [file_info[0]]
                    std = True
                i += 1
                text1 = False
                try:
                    pip_data = subprocess.check_output(value)
                    if std:
                        with open('in_out.txt', 'w') as pipe:
                            subprocess.PIPE = pipe.write(pip_data)###############need to fox the subprocess.PIPE
                    if i == x:
                        print pip_data
                except:
                    print "Error: failed open a pipe"
                    print "Error > ",sys.exc_info()[0]
            else:
                print action[i] + " is not recognized as an internal command"
                break
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