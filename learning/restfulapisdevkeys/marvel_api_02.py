#!/usr/bin/env python3

import argparse
import time
import hashlib
from pprint import pprint

import requests

API = 'http://gateway.marvel.com/v1/public/characters'

def hashbuilder(rand, privkey, pubkey):
    return hashlib.md5((f"{rand}{privkey}{pubkey}").encode('utf-8')).hexdigest()


def marvelcharcall(rand, keyhash, pubkey, lookmeup):
    r = requests.get(f"{API}?name={lookmeup}&ts={rand}&apikey={pubkey}&hash={keyhash}")
    if r.status_code != 200:
        response = None
    else:
        response = r.json()
    return response


def main():
    with open(args.dev) as pkey:
        privkey = pkey.read().rstrip('\n')

    with open(args.pub) as pkey:
        pubkey = pkey.read().rstrip('\n')

    rand = str(time.time()).rstrip('.')
    keyhash = hashbuilder(rand, privkey, pubkey)
    result = marvelcharcall(rand, keyhash, pubkey, args.hero)
    pprint(result)


if __name__ == '__main__':
    parser = argparse.ArgumentParser()
    parser.add_argument('--dev', help='Provide the /path/to/file.priv containing Marvel private developer key')
    parser.add_argument('--pub', help='Provide the /path/to/file.pub containing Marvel public developer key')
    parser.add_argument('--hero', help='Character to search for within the Marvel universe')
    args = parser.parse_args()
    main()

