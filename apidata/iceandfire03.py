#!/usr/bin/python3

import requests

AOIF_BOOKS = "https://www.anapioficeandfire.com/api/books"

def main():
    gotresp = requests.get(AOIF_BOOKS)
    got_dj = gotresp.json()

    for singlebook in got_dj:
        print(f"{singlebook['name']}, pages - {singlebook['numberOfPages']}")
        print(f"\tAPI URL -> {singlebook['url']}\n")
        print(f"\tISBN -> {singlebook['isbn']}\n")
        print(f"\tPUBLISHER -> {singlebook['publisher']}\n")
        print(f"\tNo. of CHARACTERS -> {len(singlebook['characters'])}\n")

if __name__ == "__main__":
    main()
