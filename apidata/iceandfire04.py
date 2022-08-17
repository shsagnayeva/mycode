#!/usr/bin/python3

import requests
import pprint

AOIF_CHAR = "https://www.anapioficeandfire.com/api/characters/"

def main():
    got_charToLookup = input("Pick a number between 1 and 1000 to return info on a GoT character! " )
    gotresp = requests.get(AOIF_CHAR + got_charToLookup)
    got_dj = gotresp.json()
    pprint.pprint(got_dj)

if __name__ == "__main__":
    main()
    
