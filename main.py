from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import numbeo_scraper as ns
import get_bea_data as gbd
import population_cleanup as pc
import recent_pop_cleanup as rpc


# read in population (1790 - 2010) and rj metrics meetup info (2013-2014) and merge df's
pop_df = pc.get_pop_data('data/1790-2010_MASTER.csv')
rj_df = pc.get_rj_data('data/rj_metrics.txt')
new_df = pd.concat([pop_df, rj_df], axis=1)

# clean and join bureau of economic affairs info

raw_bea = gbd.get_bea_data('http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls')
bea_df = gbd.clean_me(raw_bea)
bea_df = bea_df[:-2]
next_df = pd.concat([new_df, bea_df[bea_df['bea_2014'] > 20000]], axis=1)

# incorporate numbeo data:

url_prefix = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title='
url_suffix = '&region=021'
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']

urls = ns.build_urls(year_list)
for url in urls:
    soup_can = ns.get_pages(url)
table_list = [ns.clean_up(soup) for soup in soup_can]
zipped = list(zip(year_list, table_list))
df_dict = ns.build_data_frames(zipped)

for item in year_list:
    columns= ns.fix_em(['Rank','City','Cost of Living Index','Rent Index','Cost of Living Plus Rent Index',
          'Groceries Index','Restaurant Price Index','Local Purchasing Power Index'])
    first_cols = columns[:2]
    first_cols.extend([column + '_{}'.format(item)for column in columns[2:]])
    df_dict[item].columns = first_cols

def clean_up_df(df):
    df['state'] = df['city'].apply(lambda x: x.split(',')[1].strip().lower().replace(' ', '_'))
    df['city'] = df['city'].apply(lambda x: x.split(',')[0].lower().replace(' ', '_'))
    del df['rank']
    return df

df_2009 = clean_up_df(df_dict['2009'])
df_2010 = clean_up_df(df_dict['2010'])
df_2011 = clean_up_df(df_dict['2011'])
df_2012 = clean_up_df(df_dict['2012'])
df_2013 = clean_up_df(df_dict['2013'])
df_2014 = clean_up_df(df_dict['2014'])
df_2015 = clean_up_df(df_dict['2015'])
df_2016 = clean_up_df(df_dict['2016'])

df_list = [df_2009, df_2010, df_2011, df_2012, df_2013, df_2014, df_2015, df_2016]

def merger(df1, df2):
    df_merge = pd.merge(df1, df2,
              left_on=['city', 'state'],
              right_on=['city', 'state'],
              how='outer')
    return df_merge

merged1 = merger(df_list[0], df_list[1])
merged2 = merger(merged1, df_list[2])
merged3 = merger(merged2, df_list[3])
merged4 = merger(merged2, df_list[4])
merged5 = merger(merged2, df_list[5])
merged6 = merger(merged2, df_list[6])
merged7 = merger(merged2, df_list[7])
merged7.set_index('city', inplace=True)
value_list = ['canada', 'bermuda']
merged7 = merged7[~merged7['state'].isin(value_list)]

next_df.index.name = 'city'
next_df.reset_index(inplace=True)
merged7.reset_index(inplace=True)
next_merged_df = pd.merge(next_df, merged7, left_on='city', right_on='city', how='outer')
next_merged_df.set_index('city', inplace=True)
# 18 data frames successfully merged!!!!

globule = glob.glob('/Users/IXChris/Desktop/G/capstone/data/biggestuscities/cities/*.csv')
pop_df = rcp.recent_pop_merger(globule)

next_merged_df.reset_index(inplace=True)
pop_df.reset_index(inplace=True)

master_merger_df = (pd.merge(next_merged_df, pop_df, left_on='city', right_on='city', how='outer'))
