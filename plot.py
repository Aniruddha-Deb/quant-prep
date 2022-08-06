#!/usr/bin/env python

import pandas as pd
import matplotlib.pyplot as plt
import sys

def plot(filename):
    df = pd.read_csv(filename,header=None,parse_dates=[0])
    
    df = df.loc[(df[1] > 30) & (df[1] < 70)]

    plt.scatter(df[0],df[1])
    plt.show()

if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("Plot: Missing required argument <datafile>")
    else:
        plot(sys.argv[1])
