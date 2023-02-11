import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import string


class Analysis:
    def sample_plot():
        sp500 = pd.read_csv('./data/SP500.csv')

        sp500['DATE'] = pd.to_datetime(sp500['DATE'], format='%Y-%m-%d')
        sp500['SP500'] = pd.to_numeric(sp500['SP500'], errors='coerce')
        sp500['SP500'] = sp500['SP500'].dropna()

        return Analysis.linear_plot(sp500['DATE'], sp500['SP500'])


    def linear_plot(x,y):
        plt.clf()
        plt.plot(x,y)
       
        filename = './static/plot.png'
        plt.savefig(filename)

        return filename
