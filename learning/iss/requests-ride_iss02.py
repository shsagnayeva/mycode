#!/usr/bin/python3

import urllib.request
import json

MAJORTOM = "http://api.open-notify.org/astros.json"

def main():
    groundctrl = urllib.request.urlopen(MAJORTOM)
    helmet = groundctrl.read()
    helmetson = json.loads(helmet.decode("utf-8"))
    print("People in space: " + str(helmetson["number"]))

    for astro in helmetson["people"]:
        print(astro["name"] + " on the " + astro["craft"])

if __name__ == "__main__":
    main()

