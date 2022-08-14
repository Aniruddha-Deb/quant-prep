#!/usr/bin/env python

import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import sys

def plot(filename):
    df = pd.read_csv(filename,header=None,parse_dates=[0])
    
    df = df.loc[(df[1] > 30) & (df[1] < 70)] # exclude warmup runs/outliers

    cfft = np.polyfit(df[0].map(lambda x: x.timestamp()),df[1],1)
    p1d_fn = np.poly1d(cfft)

    plt.plot(df[0],df[1],'bo',df[0],p1d_fn(df[0].map(lambda x: x.timestamp())), '--k')
    plt.title("# of problems solved in 2 min, default settings on Zetamac")
    plt.ylim(30,60)
    fig = plt.gcf()
    fig.autofmt_xdate(rotation=45)
    ax = plt.gca()
    ax.axvline(pd.to_datetime('2022-07-25T20:00:00'), color='r')

    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Plot: Missing required argument <datafile>")
    else:
        plot(sys.argv[1])
