#!/usr/bin/env python3

# create a small string
newstring = "a b c d e f"
newlist = newstring.split(" ") # this returns a list
print(newlist)

# create a list of strings
mylist = ["10092", "11168", "2220", "144862"]

# create a string with join() method
singlestr = ".".join(mylist)

# display singlestr
print(singlestr)

