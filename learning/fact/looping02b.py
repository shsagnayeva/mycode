#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:
    
    # create list of lines
    dnslist = dnsfile.readlines()

    for svr in dnslist:
        #print and end without a newline
        print(svr, end="")


