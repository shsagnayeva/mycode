#!/usr/bin/env python3

import requests

API = "https://api.magicthegathering.io/v1/"

def main():
    setcode = input("What is the code of the set you are trying to lookup (see mtgsets.index for a list of codes)? ").lower()
    resp = requests.get(f"{API}cards?set={setcode}")
    cards = resp.json()
    print(cards)

if __name__ == "__main__":
    main()


