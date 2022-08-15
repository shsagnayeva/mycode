#!/usr/bin/python3

import pandas as pd

def main():
    df = pd.read_csv("5movies.csv")
    df.to_excel("5movies-translated-from-json.xlsx")

if __name__ == "__main__":
    main()

