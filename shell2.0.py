# -*- coding: utf-8 -*-
"""
date: 25/10/2018
Name: shell project
Yotam Levit
"""
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
ERR_OPEN_PIPE = "Error: failed open a pipe"
ERR_NOT_VALID = " is not recognized as an internal command"
ERR_NOT_VALID_PIPE = "invalid pip"
STDIN_FILE = 'in_out.txt'
PYTHON = "python"
NONE = "None"
SPACE = "space"
EMPTY = ""
SLASH = "/"
SPACE_ST = " "


def write_and_open_stdin(pip_data):
    """
    Write to the stdin file the updated pipe data
    that should go through the pipe then open the
    file and return the file object
    ;pip_data: the data that should go through the pipe
    return: the stdin file object
    """
    with open(STDIN_FILE, 'w') as pipe:
        pipe.write(pip_data)
    file_obj = open(STDIN_FILE, 'r')
    return file_obj


def detect_file(tool, path):
    """
    Fill the  path that is given for the command adding it`s kind
    py or exe (python or an exe file), the path that is returned can be mistake
    ;tool: the command name
    ;path: the path that the function will fill
    return: the filled path and its kind (python or an exe file)
    """
    temp = path.split(SLASH)
    if temp[len(temp)-1] == "Shell":
        return [path + SLASH + tool + ".py", PYTHON]
    else:
        return [path + SLASH + tool + ".exe", "exe"]


def find_path(action):
    """
    Searches the correct path of a command
    in the paths string
    ;action: the command name
    return: the correct path of the given command
    """
    did_it = False
    found = NONE
    for path in PATH_TO_TOOL.split(";"):
        if did_it:
            break
        if is_file(action, path):
            found = path
            did_it = True
    return found


def is_file(tool, path):
    """
    Check if a path of a command exists or not
    return: True if path exist
            False if path not exist
    """
    return os.path.isfile(detect_file(tool, path)[0])


def get_action(user_input):
    """
    Get from the user input the commands
    ;user_input: the input that the user gave
    return: a list of the command that were given
            (if a space was needed for the action there
            will be a space action in the list and after
             the specific function that the exe command needs
             for example: ipconfig /renew or where notepad)
    """
    temp = user_input.split("|")
    action = []
    for t in temp:
        s = t.lstrip(SPACE_ST)
        s = s.split(SPACE_ST)
        if s[0] != SPACE_ST:
            action.append(s[0])
            if len(s) > 1 and s[1] != EMPTY:
                temp1 = action.pop()
                action.append(SPACE)
                action.append(temp1)
                action.append(s[1])
    return action


def run_std(action, i, file_obj, pip_data, path):
    """
    run the command with the stdin that it needs according to the user
    ;action: a list of the commands
    ;i: the index at the list operation loop
    ;file_obj: stdin object file
    ;pip_data: the pipe optional arguments
    ;path: the command`s path
    return: the next index at the list operation loop
            if the function should run again
            the stdin object file (None if there is no new one)
            the updated pipe optional arguments
    """
    file_info = detect_file(action[i], path)
    if file_info[1] == PYTHON:
        if pip_data != EMPTY:
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
            file_obj = write_and_open_stdin(pip_data)
            return i, True, file_obj, pip_data
    except:
        print ERR_OPEN_PIPE
        print "Error > ", sys.exc_info()[0]
    return i, False, None, pip_data


def run_space(action, i, path):
    """
    run a exe command with the specific function that
     it needs according to the user
    ;action: a list of the commands
    ;i: the index at the list operation loop
    ;path: the command`s path
    return: the next index at the list operation loop
            the updated pipe optional arguments
    """
    file_info = detect_file(action[i], path)
    value = [file_info[0]] + [action[i+1]]
    i += 2
    try:
        pip_data = subprocess.check_output(value)
        if i == len(action):
            print pip_data
    except:
        print ERR_OPEN_PIPE
        print "Error > ", sys.exc_info()[0]
    return i, pip_data


def run_command(action, path, pip_data, i, std):
    """
    run the command according to the user or with
     the the pipe optional arguments if needed
     or just run the command
    ;action: a list of the commands
    ;i: the index at the list operation loop
    ;pip_data: the pipe optional arguments
    ;path: the command`s path
    ;std: if the run_std() function should be operated
    return: the next index at the list operation loop
            the stdin object file (None if there is no new one)
            if the run_std() function should be operated
            the updated pipe optional arguments
    """
    file_info = detect_file(action[i], path)
    if file_info[1] == PYTHON:
        if pip_data != EMPTY:
            value = [file_info[1], file_info[0]] + [pip_data]
        else:
            value = [file_info[1], file_info[0]]
    else:
        value = [file_info[0]]
        std = True
    i += 1
    try:
        pip_data = subprocess.check_output(value)
        if std:
            file_obj = write_and_open_stdin(pip_data)
        if i == len(action):
            print pip_data
        if std:
            return i, file_obj, std, pip_data
    except:
        print ERR_OPEN_PIPE
        print "Error > ", sys.exc_info()[0]
    return i, None, std, pip_data


def convert_low(action):
    """
    convert all commands to lowercase
    ;action: list of commands
    return: list of commands in lowercase
    """
    i = 0
    for a in action:
        action[i] = a.lower()
        i += 1
    return action


def run(user_input):
    """
    the function runs the user`s commands using a loop with piping and errors
    ;user_input: the input that the user gave to the shell to do
    """
    action = get_action(user_input)
    x = len(action)
    i = 0
    text1 = False
    space = False
    std = False
    pip_data = EMPTY
    action = convert_low(action)
    while i < x:
        if action[i] == "hello" and x == 1:
            pip_data = SPACE_ST
        if std:
            path = find_path(action[i])
            if path != NONE:
                i, std, file_obj, pip_data =\
                    run_std(action, i, file_obj, pip_data, path)
        elif space:
            path = find_path(action[i])
            if path != NONE:
                i, pip_data = run_space(action, i, path)
                space = False
            else:
                print action[i] + ERR_NOT_VALID
                break
        elif action[i] == SPACE:
            space = True
            i += 1
        elif ".txt" in action[i]:
            pip_data = action[i]
            if text1:
                print ERR_NOT_VALID_PIPE
                break
            text1 = True
            i += 1
        else:
            path = find_path(action[i])
            if path != NONE:
                text1 = False
                i, file_obj, std, pip_data =\
                    run_command(action, path, pip_data, i, std)
            else:
                if i+1 < x:
                    pip_data = action[i]
                    i += 1
                else:
                    print action[i] + ERR_NOT_VALID
                    break


def main():
    """
    the main function, control the basic decisions
    the function decides whether to execute the
    user commands or not and if close the shell or not
    """
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