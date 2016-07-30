from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import get_bea_data as gbd

def get_pop_data(file_path='data/1790-2010_MASTER.csv'):
    '''
    INPUT: File path to US census population csv file
    OUTPUT: DataFrame of pop data of top 100 US cities 1790:2010
    '''
    df = pd.read_csv(file_path)
    df['City'] = df['City'].apply(lambda x: x.lower().replace(' ', '_').replace('-','_'))
    df['City'].replace({'new_york_city': 'new_york'}, inplace=True)
    df.set_index(['City'], inplace=True)
    df.sort_values(by=['2010'], ascending=False, inplace=True)
    # FIX THIS TO JOIN BY STATE TO GET MORE CITIES
    df = df.head(111)
    df['STPLFIPS_2010']=df['STPLFIPS_2010'].astype(int)
    # 'Name_2010',
    df.drop(['Place Type','CityST', 'ID','LAT_BING', 'LON_BING', '1790','1800','1810', '1820', '1830', '1840', '1850', '1860', '1870', '1880', '1890', '1900', '1910', '1920',
        '1930', '1940',], axis=1, inplace=True)
    return df

def get_rj_data(file_path='data/rj_metrics.txt'):
    '''
    INPUT: File path to rj metrics text file
    OUTPUT: Cleaned dataFrame of file
    '''
    rj_df = pd.read_table(file_path)
    rj_df['state'] = (rj_df['City'].apply(lambda x: x.split(',')[-1]))
    rj_df['city'] = rj_df['City'].apply(lambda x: x.lower().split(',')[0])
    rj_df['city'] = rj_df['city'].apply(lambda x: x.replace(' ', '_').replace('-','_'))
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
