from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns
import os


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

# buruea of economic affiars clean and join
bea_df = pd.read_csv('data/bea.csv', header=2)
columns = bea_df.columns
new_columns = [u'city', u'bea_state', u'bea_2009', u'bea_2010', u'bea_2011', u'bea_2012', u'bea_2013', u'bea_2014', u'bea_what_is_this _crap']
bea_df.columns = new_columns
#bea_df = bea_df[1:]
bea_df['city'] = bea_df['bea_state'].apply(lambda x: x.split(',')[0])
bea_df['city'] = bea_df['city'].apply(lambda x: x.lower().replace('-', '_').replace(' ', '_'))
bea_df['bea_state'] = bea_df['bea_state'].apply(lambda x: x.split(',')[-1])
bea_df.set_index('city', inplace=True)

next_df = pd.concat([new_df, bea_df], axis=0)
