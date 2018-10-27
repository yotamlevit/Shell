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

def run_std(action, i, file_obj, pip_data, path):
    file_info = detect_file(action[i], path)
    if file_info[1] == "python":
        if pip_data != "":
            value = [file_info[1], file_info[0]]
    else:
        value = [file_info[0]]
    i += 1
    try:
        pip_data = subprocess.check_output(value, stdin=file_obj)
        if i == len(action):
            print pip_data
            file_obj.close()
        else:
            with open('in_out.txt', 'w') as pipe:
                pipe.write(pip_data)
            file_obj = open('in_out.txt', 'r')
            return i, True, file_obj, pip_data
    except:
        print "Error: failed open a pipe"
        print "Error > ", sys.exc_info()[0]
    return i, False, None, pip_data


def run_space(action, i, path):
    file_info = detect_file(action[i], path)
    value = [file_info[0]] + [action[i+1]]
    i += 2
    try:
        pip_data = subprocess.check_output(value)
        if i == len(action):
            print pip_data
    except:
        print "Error: failed open a pipe"
        print "Error > ", sys.exc_info()[0]
    return i, pip_data


def run_command(action, path, pip_data, i, std):
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
                pipe.write(pip_data)
            file_obj = open('in_out.txt', 'r')
        if i == len(action):
            print pip_data
        if std:
            return i, file_obj, text1, std, pip_data
    except:
        print "Error: failed open a pipe"
        print "Error > ", sys.exc_info()[0]
    return i, None, text1, std, pip_data

def run(input1):
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
                i, std, file_obj, pip_data = run_std(action, i, file_obj, pip_data, path)
        elif space:
            path = find_path(action[i])
            if path != "None":
                i, pip_data = run_space(action, i, path)
                space = False
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
                i, file_obj, text1, std, pip_data = run_command(action, path, pip_data, i, std)
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

            print "Thx for using the exit command"
        else:
            run(input_)

if __name__ == '__main__':
    main()