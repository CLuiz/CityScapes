from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os
import get_bea_data as gbd


df = pd.read_csv('data/1790-2010_MASTER.csv')
df.set_index(['City'], inplace=True)
df.sort_values(by=['2010'], ascending=False, inplace=True)
df = df.head(100)

df['STPLFIPS_2010']=df['STPLFIPS_2010'].astype(int)
df.drop(['Name_2010','Place Type','CityST', 'ID','LAT_BING', 'LON_BING'], axis=1, inplace=True)

columns = df.columns

rj_df = pd.read_table('data/rj_metrics.txt')
rj_df['state'] = (rj_df['City'].apply(lambda x: x.split(',')[-1]))
rj_df['city'] = rj_df['City'].apply(lambda x: x.split(',')[0])
rj_df.drop('City', axis =1, inplace=True)
rj_df.set_index(['city'], inplace = True)

new_df = pd.concat([df, rj_df], axis=1)
meetup_df = new_df[new_df['Pop'].notnull()]
cities = list(meetup_df.index)

# bureau of economic affairs clean and join
url = 'http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls'
raw_bea = gbd.get_bea_data(url)
bea_df = gbd.clean_me(raw_bea)
next_df = pd.concat([new_df, bea_df], axis=0)
