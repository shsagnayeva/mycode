#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:

    for svr in dnsfile:
        # print and end without a newline
        print(svr, end="")
