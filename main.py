from __future__ import division
import pandas as pd
import numpy as np
import matplotlib.pyplot as plt
import os
import numbeo_scraper as ns
import get_bea_data as gbd
import population_cleanup as pc
import recent_pop_cleanup as rpc
import glob
import walkscore as ws
import os

# read in population (1790 - 2010) and rj metrics meetup info (2013-2014) and merge df's
census_pop_df = pc.get_pop_data('data/1790-2010_MASTER.csv')
rj_df = pc.get_rj_data('data/rj_metrics.txt')
new_df = pd.concat([census_pop_df, rj_df], axis=1)

print 'Census data merged to RJ metrics data!'
# clean and join bureau of economic affairs info

raw_bea = gbd.get_bea_data('http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls')
bea_df = gbd.clean_me(raw_bea)
bea_df = bea_df[:-2]
next_df = pd.concat([new_df, bea_df[bea_df['bea_2014'] > 20000]], axis=1)
print 'Bureau of Economic Affairs data merged!'
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
merged4 = merger(merged3, df_list[4])
merged5 = merger(merged4, df_list[5])
merged6 = merger(merged5, df_list[6])
merged7 = merger(merged6, df_list[7])
merged7.set_index('city', inplace=True)
value_list = ['canada', 'bermuda']
merged7 = merged7[~merged7['state'].isin(value_list)]

next_df.index.name = 'city'
next_df.reset_index(inplace=True)
merged7.reset_index(inplace=True)
next_merged_df = pd.merge(next_df, merged7, left_on='city', right_on='city', how='outer')
next_merged_df.set_index('city', inplace=True)
# 18 data frames successfully merged!!!!
print 'Numbeo data merged!'
globule = glob.glob('/Users/IXChris/Desktop/G/capstone/data/biggestuscities/cities/*.csv')
pop_df = rpc.recent_pop_merger(globule)

next_merged_df.reset_index(inplace=True)
pop_df.reset_index(inplace=True)

master_merger_df = (pd.merge(next_merged_df, pop_df, left_on='city', right_on='city', how='outer'))
print 'Recent population data merged!'
master_merger_df['state_y'].fillna(master_merger_df['state_x'], inplace=True)
master_merger_df['state_y'].fillna(master_merger_df['ST'], inplace=True)
master_merger_df['state_y'].fillna(master_merger_df['bea_state'], inplace=True)
master_merger_df['state'] = master_merger_df['state_y']
master_merger_df['state'] = master_merger_df['state'].str.lower()
cols = master_merger_df.columns
cols= [str(col).lower() for col in cols]
master_merger_df.columns = cols

del master_merger_df['state_y']
del master_merger_df['state_x']
del master_merger_df['index']
del master_merger_df['st']
del master_merger_df['bea_state']

# read in and merge walkscore data:
url = 'https://www.walkscore.com/cities-and-neighborhoods/'
walk_data = ws.get_walk_data(url)
# strip off Australian cities:
#walk_data = walk_data[:-42]
walk_df = ws.data_framify(walk_data)
walk_df.set_index(['city', 'state'], inplace=True)
master_merger_df.reset_index()
master_merger_df['state'].str.lower()
master_merger_df.set_index(['city', 'state'], inplace=True)
df_with_walkscore = pd.concat([master_merger_df, walk_df], axis=1)
# build in an if path exists thing here
print 'Walkscore data merged!'

# incorporate air traffic data:
path = os.getcwd()
filename = '/data/airtraffic.csv'
file_path = path + filename
air_df = pd.read_csv(file_path)
air_df.set_index(['city', 'state'], inplace=True)
df_with_walkscore.reset_index(inplace=True)
df_with_walkscore.set_index(['city', 'state'], inplace=True)
df_with_air_traffic = pd.concat([df_with_walkscore, air_df], axis=1)
print "Air traffic data merged"

# get ready for modelling!
dense_2013 = master_merger_df[master_merger_df['2013'].notnull() ==True]
'''
lets cluster on only data from 2013!!!
'''
dense_2013.reset_index(inplace=True)
# = master_merger_df[master_merger_df['pop'].notnull()]
cols = [u'city',u'pop', u'total members',u'members (% of pop)',u'% growth 2013',u'members of largest group',u'cost_of_living_index_2013', u'rent_index_2013', u'groceries_index_2013', u'restaurant_price_index_2013', u'local_purchasing_power_index_2013']

dense_2013 = dense_2013[cols]
dense_2013= dense_2013[dense_2013['pop'].notnull()]
dense_2013.set_index('city', inplace=True)
#dense_test_df.drop('bea_2013', axis=1, inplace=True)
dense_2013.drop('boulder', axis=0, inplace=True)
