#!/usr/bin/python3

import pandas as pd
import seaborn as sns
import matplotlib
matplotlib.use('Agg')

def main():
    opsd_daily = pd.read_csv('netTraffic.csv', index_col=0, parse_dates=True)
    opsd_daily['Year'] = opsd_daily.index.year
    opsd_daily['Month'] = opsd_daily.index.month
    opsd_daily['Weekday Name'] = opsd_daily.index.day_name()
    
    sns.set(rc={'figure.figsize':(11, 4)})
    netlineplot = opsd_daily['Consumption'].plot(linewidth=0.5)
    
    fig = netlineplot.get_figure()
    fig.savefig("/home/student/static/linePlot.png")

    cols_plot = ['Consumption', 'YouTube', 'Netflix']
    axes = opsd_daily[cols_plot].plot(marker='.', alpha=0.5, linestyle='None', figsize=(11, 9), subplots=True)

    for ax in axes:
        ax.set_ylabel('Daily Totals (TBs)')

        # save out this figure
        fig = ax.get_figure()
        fig.savefig(f"/home/student/static/dotPlot.png")

if __name__ == "__main__":
    main()

