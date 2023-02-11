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

        plt.clf()
        plt.plot(sp500['DATE'], sp500['SP500'])

        filename = './static/plot.png'
        plt.savefig(filename)

        return filename
