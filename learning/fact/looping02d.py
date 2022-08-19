#!/usr/bin/env python3

# open file in read mode
with open("dnsservers.txt", "r") as dnsfile:

     for svr in dnsfile:
        svr = svr.rstrip('\n') # remove newline char if exists

        if svr.endswith('org'):
            with open("org-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")

        elif svr.endswith('com'):
            with open("com-domain.txt", "a") as srvfile:  # 'a' is append mode
                srvfile.write(svr + "\n")


