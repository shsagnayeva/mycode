#!/usr/bin/env python3

import json

def commandpush(devicecmd):

    for ip in devicecmd.keys():
        print(f'Handshaking. .. ... connecting with {ip}')

        for mycmds in devicecmd[ip]:
            print(f'Attempting to sending command --> {mycmds}')

    return None

def main():

    with open("devicecmd.json", "r") as devicecmdfile:
        devicecmd = json.load(devicecmdfile)

    print("Welcome to the network device command pusher")

    print("\nData set found\n")

    commandpush(devicecmd)

main()

