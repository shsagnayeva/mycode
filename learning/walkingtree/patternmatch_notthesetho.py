#!/usr/bin/env python3

"""Script to search for a pattern match"""

import os
import fnmatch 

EXCLUDE = ["/usr", "/home", "/var"] 

def find(pattern, path):

    result = []
    for root, dirs, files in os.walk(path, topdown=True):
        if root in EXCLUDE: # if the root matches the exclude list
            dirs[:] = [] # remove the directory list for this iteration
            files[:] = [] # remove the file list for this iteration
        for name in files: # always perform the nested loop, but it maybe empty
            if fnmatch.fnmatch(name, pattern): # if match
                result.append(os.path.join(root, name))
    return result 

def main():

    lookfor = input("What pattern am I looking for (Example: *.txt or *.cfg) ")
    lookwhere = input("What is the path in which I should search? ")
    print("Results: ", find(lookfor, lookwhere)) 

if __name__ == "__main__":
    main()

