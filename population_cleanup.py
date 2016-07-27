from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import get_bea_data as gbd

def get_pop_data(file_path='data/1790-2010_MASTER.csv'):
    df = pd.read_csv(file_path)
    df.set_index(['City'], inplace=True)
    df.sort_values(by=['2010'], ascending=False, inplace=True)
    df = df.head(100)
    df['STPLFIPS_2010']=df['STPLFIPS_2010'].astype(int)
    df.drop(['Name_2010','Place Type','CityST', 'ID','LAT_BING', 'LON_BING'], axis=1, inplace=True)
    return df

def get_rj_data(file_path='data/rj_metrics.txt'):
    rj_df = pd.read_table(file_path)
    rj_df['state'] = (rj_df['City'].apply(lambda x: x.split(',')[-1]))
    rj_df['city'] = rj_df['City'].apply(lambda x: x.lower().split(',')[0])
    rj_df.drop('City', axis =1, inplace=True)
    rj_df.set_index(['city'], inplace = True)
    return rj_df


if __name__ == '__main__':
    new_df = pd.concat([df, rj_df], axis=1)
    meetup_df = new_df[new_df['Pop'].notnull()]
    cities = list(meetup_df.index)

    # bureau of economic affairs clean and join
    url = 'http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls'
    raw_bea = gbd.get_bea_data(url)
    bea_df = gbd.clean_me(raw_bea)
    next_df = pd.concat([new_df, bea_df], axis=0)
