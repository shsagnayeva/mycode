#!/usr/bin/python3

import requests

def astros():
    r = requests.get("http://api.open-notify.org/astros.json")
    if r.status_code == 200:
        return r.json()
    else:
        return None

def main():
    print("Right now in space we have...")
    print(astros())


if __name__ == "__main__":
    main()

