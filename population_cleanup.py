import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import seaborn as sns

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
