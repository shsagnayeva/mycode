#!/usr/bin/env python3

# open file in read mode
dnsfile = open("dnsservers.txt", "r")

# create list of lines
dnslist = dnsfile.readlines()

for svr in dnslist:
    # print and end without a newline, the line we read ALREADY contains a \n (newline)
    print(svr, end="")

dnsfile.close()


