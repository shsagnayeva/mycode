#!/usr/bin/python3

import yaml

def main():
    with open("myYAML.yml", "r") as yf:
        pyyammy = yaml.load(yf, Loader=yaml.FullLoader)

    print(pyyammy)

if __name__ == "__main__":
    main()

