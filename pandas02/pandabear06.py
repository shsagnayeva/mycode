#!/usr/bin/python3

import pandas as pd

def main():
    opsd_daily = pd.read_csv('netTraffic.csv')
    print(opsd_daily.shape)
    print("\nLook at the first three rows")
    print(opsd_daily.head(3))
    print("\nLook at the last three rows")
    print(opsd_daily.tail(3))
    print(opsd_daily.dtypes)
    
    opsd_daily = opsd_daily.set_index('Date')
    print("\nLook at the first three rows after date has been set as the primary index")
    print(opsd_daily.head(3))
    print("\nLook at the last three rows after date has been set as the primary index")
    print(opsd_daily.tail(3))
    input("\nPress ENTER to look at all of the index values associated with the dataset (dates)")
    print(opsd_daily.index)

    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()

    input("\nPress ENTER to look at a random sampling from 5 rows after adding the Year, Month and Weekday Name columns")
    print(opsd_daily.sample(5, random_state=0))

if __name__ == "__main__":
    main()
