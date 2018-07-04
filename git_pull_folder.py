#!/usr/bin/env python3
##-------------------------------------------------------------------
##  @copyright 2018 DennyZhang.com
## Licensed under MIT
##   https://www.dennyzhang.com/wp-content/mit_license.txt
##
## File: git_pull_folder.py
## Author : Denny <https://www.dennyzhang.com/contact>
## Description : https://github.com/dennyzhang/git_pull_folder
## --
## Created : <2018-07-03>
## Updated: Time-stamp: <2018-07-03 17:17:57>
##-------------------------------------------------------------------
import os, sys
import subprocess

def git_pull_folder(folder):
    # git pull origin "$(git branch | awk -F' ' '{print $2}')"
    try:
        command = "cd %s && git pull origin \"$(git branch | awk -F' ' '{print $2}')\"" % (folder)
        print(command)
        command_output = subprocess.check_output(command, shell = True, stderr=subprocess.STDOUT)
    except subprocess.CalledProcessError as grepexc:
        print("Error. code: %d, errmsg: %s" % (grepexc.returncode, grepexc.output))
        sys.exit(1)

def git_pull(folder, max_depth):
    print("Run git pull recursively under:" + folder)

    import collections
    queue = collections.deque()
    queue.append(folder)
    for i in range(max_depth):
        while len(queue) != 0:
            for i in range(len(queue)):
                element = queue.popleft()
                l = os.listdir(element)
                if ".git" in l:
                    git_pull_folder(element)
                else:
                    for f in l:
                        path = "%s/%s" % (element, f)
                        if os.path.isdir(path): queue.append(path)
    print("Git pull is done")

if __name__ == '__main__':
    import argparse
    parser = argparse.ArgumentParser()
    parser.add_argument('--folder', default='', required=False,
                        help="Which folder to run git pull. If not given, it's current directory'", type=str)

    parser.add_argument('--max_depth', default='2', required=False,
                        help="How many indepth we want to look inside the folder", type=int)

    l = parser.parse_args()
    folder = l.folder
    if folder == "": folder = os.getcwd()
    git_pull(folder, l.max_depth)
## File: git_pull_folder.py ends
