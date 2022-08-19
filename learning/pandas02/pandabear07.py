#!/usr/bin/python3

import pandas as pd

def main():
    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    input("\nPress ENTER to see the data for 2017-08-10")
    print(opsd_daily.loc['2017-08-10'])

    input("\nPress ENTER to see the data slice from 2014-01-20 to 2014-01-22")
    print(opsd_daily.loc['2014-01-20':'2014-01-22'])

    input("\nPress ENTER to see the data slice for 2012-02")
    print(opsd_daily.loc['2012-02'])

if __name__ == "__main__":
    main()

