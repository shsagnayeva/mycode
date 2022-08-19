#!/usr/bin/env python3

import re
import requests

def main():
    while(True):
        print("Where should we search?. Type 'q' to exit")
        url = input("> ")
        if url == "q" or url == "Q":
            break
        else:
            print(f"Great! So we'll try to open this URL {url} to search for the phrase:")
            searchFor = input("> ")
            resp = requests.get(url)  # Send HTTP GET
            searchMe = resp.text

            if re.search(searchFor, searchMe):
                print("Found a match!")
            else:
                print("No match!")

if __name__ == "__main__":
    main()
