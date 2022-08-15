#!/usr/bin/env python3

import re
import requests

def main():
    print("Where should we search?")
    url = input("> ")

    print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
    searchFor = input("> ")

    resp = requests.get(url)  
    searchMe = resp.text

    if re.search(searchFor, searchMe):
        print("Found a match!")
    else:
        print("No match!")

if __name__ == "__main__":
    main()
