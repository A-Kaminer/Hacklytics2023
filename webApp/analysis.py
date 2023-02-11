import numpy as np
import matplotlib.pyplot as plt
import pandas as pd
import os
import string
import datetime


class Analysis:

    def __init__(self):
        self.data = self.parse_data()


    def parse_data(self):
        sp500 = pd.read_csv('./data/SP500.csv')
        dff = pd.read_csv('./data/DFF.csv').iloc[1:]
        dr = pd.read_csv('./data/DRALACBN.csv')

        sp500['DATE'] = pd.to_datetime(sp500['DATE'], format='%Y-%m-%d')
        sp500['SP500'] = pd.to_numeric(sp500['SP500'], errors='coerce')
        sp500['SP500'] = sp500['SP500'].dropna()
        sp500 = sp500.set_index('DATE')
        sp500 = sp500 / 1000

        sp = pd.read_csv('data/old_SP500.csv')
        sp = sp.rename(columns={'Price':'SP500', 'Date':'DATE'})
        sp = sp.drop(columns=['Open', 'High', 'Low', "Vol.", 'Change %'])
        sp['DATE'] = pd.to_datetime(sp['DATE'], format='%m/%d/%Y')
        sp['SP500'] = sp['SP500'].replace(',', '', regex=True)
        sp['SP500'] = pd.to_numeric(sp['SP500'])
        sp = sp.set_index('DATE')
        sp = sp / 1000
        sp500 = pd.concat([sp500, sp], axis=0).sort_index()

        dff = dff.rename(columns={'FEDFUNDS':'DFF'})
        dff['DATE'] = pd.to_datetime(dff['DATE'], format='%Y-%m-%d')
        dff['DFF'] = pd.to_numeric(dff['DFF'], errors='coerce')
        dff['DFF'] = dff['DFF'].dropna()
        dff = dff.set_index('DATE')

        dr = pd.read_csv('data/FRB_CHGDEL.csv')
        dr = dr.iloc[5:]
        dr = dr.rename(columns={'Series Description':'DATE', 
                                   'Delinquency rate on all loans; All commercial banks (Seasonally adjusted)':'DR'})
        dr = dr.loc[:, ['DATE', 'DR']]
        dr.replace('Q1','-1-1', regex=True, inplace=True)
        dr.replace('Q2','-4-1', regex=True, inplace=True)
        dr.replace('Q3','-7-1', regex=True, inplace=True)
        dr.replace('Q4','-10-1', regex=True, inplace=True)
        dr['DATE'] = pd.to_datetime(dr['DATE'], format='%Y-%m-%d')
        dr['DR'] = pd.to_numeric(dr['DR'], errors='coerce')
        dr = dr.set_index('DATE')
        dr = dr.loc[datetime.datetime(2000,1,1):]
        self.impute_all_dates(dr)

        data = pd.concat([dff, dr, sp500], axis=1)
        data.interpolate(inplace=True)
        data = data.dropna()

        return data

    def sample_plot(self, is_null):
        sp500 = pd.read_csv('./data/SP500.csv')

        sp500['DATE'] = pd.to_datetime(sp500['DATE'], format='%Y-%m-%d')
        sp500['SP500'] = pd.to_numeric(sp500['SP500'], errors='coerce')
        sp500['SP500'] = sp500['SP500'].dropna()

        fig = plt.Figure()
        ax = fig.add_subplot(1,1,1)
        if not is_null == "True":
            ax.plot(sp500['DATE'], sp500['SP500'])

        return fig


    def impute_dates(self, df, start_date, end_date, step=datetime.timedelta(days=1)):
        end_date -= datetime.timedelta(days=1)
        for date in pd.date_range(start_date, end_date).to_list():
            df.loc[date] = df.loc[start_date]


    def impute_all_dates(self, df):
        indices = df.index
        for i in range(len(indices) - 1):
            self.impute_dates(df, indices[i], indices[i+1])
        df.sort_index(inplace=True)




if __name__ == '__main__':
    a = Analysis()
