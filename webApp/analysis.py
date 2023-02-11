import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import string


class Analysis:
    def make_random_plot():
        a = np.random.randint(5, size=1)[0]
        b = np.random.randint(5, size=1)[0]
        c = np.random.randint(5, size=1)[0]

        x = np.arange(-5,5,.5)
        y = x**a + x**b + c

        plt.clf()
        plt.plot(x,y)
       
        filename = f'./static/plot.png'
        plt.savefig(filename)
        return filename
