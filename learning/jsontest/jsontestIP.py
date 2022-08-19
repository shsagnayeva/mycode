#!/usr/bin/python3

import requests

IPURL = "http://ip.jsontest.com/"

def main():
    resp = requests.get(IPURL)
    respjson = resp.json()
    print(respjson)
    print(f"The current WAN IP is --> {respjson['ip']}")


if __name__ == "__main__":
    main()

