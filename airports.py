import pandas as pd
import os

tabs = pd.read_table('/Users/IXChris/Desktop/G/capstone/data/air_traffic_table.txt')

# clean up column names
cols = [u'Code', u'Major city served', u'State', u'2015[3]']
tabs.reset_index(inplace=True)
tabs = tabs[cols]
cols = [col.lower() for col in cols]
cols[1] = 'city'
cols[-1] = 'passengers'
tabs.columns = cols
tabs['city'] = tabs['city'].str.lower()
tabs['city'] = tabs['city'].map(lambda x: x.replace(' ', '_').replace('.', '').replace(',', ''))

# clean up data
second_cities = [item.split('/') for item in tabs['city'] if '/' in item]
tabs['city'] = tabs['city'].map(lambda x: x.split('/')[0])
tabs['passengers'] =tabs['passengers'].map(lambda x: int(x.replace(',', '')))
tabs['state'] = tabs['state'].map(lambda x: x.split('/')[0].lower())

# account for mulit-airports cities
fixed_dallas = tabs.loc[tabs['city'] == 'dallas', 'passengers'].sum()
fixed_chicago = tabs.loc[tabs['city'] == 'chicago', 'passengers'].sum()
fixed_new_york = tabs.loc[tabs['city'] == 'new_york', 'passengers'].sum() + tabs.loc[tabs['city'] == 'newark', 'passengers'].sum()
fixed_washington = tabs.loc[tabs['city'] == 'washington_dc', 'passengers'].sum() + tabs.loc[tabs['city'] == 'baltimore', 'passengers'].sum()
fixed_houston = tabs.loc[tabs['city'] == 'houston', 'passengers'].sum()



tabs.set_index('city', inplace=True)
tabs.set_value('dallas', 'passengers', fixed_dallas)
tabs.set_value('chicago', 'passengers', fixed_chicago)
tabs.set_value('washington_dc', 'passengers', fixed_washington)
tabs.set_value('houston', 'passengers', fixed_houston)
tabs.set_value('new_york', 'passengers', fixed_new_york)
tabs.set_value('washington_dc', 'state', 'dc')
tabs.reset_index(inplace=True)

# account for multi-city airports not working yet
baltimore = fixed_washington
newark = fixed_new_york
fort_worth = fixed_dallas


# this is working
fort_worth = tabs.loc[tabs['city'] == 'dallas']
fort_worth['city'] = 'fort_worth'
baltimore = tabs.loc[tabs['city'] == 'washington_dc']
baltimore['city'] = 'baltimore'
baltimore['state'] = 'md'
newark = tabs.loc[tabs['city'] == 'new_york']
newark['city'] = 'newark'
tacoma = tabs.loc[tabs['city'] == 'seattle']
tacoma['city'] = 'tacoma'
st_paul = tabs.loc[tabs['city'] == 'minneapolis']
st_paul['city'] = 'st_paul'
durham = tabs.loc[tabs['city'] == 'raleigh']
durham['city'] = 'durham'

# add duplicated city rows
add_cities = [tacoma, st_paul, durham, fort_worth, baltimore, newark]
tabs = tabs.append(add_cities)

# remove duplicate rows
tabs = tabs.drop_duplicates(subset='city', keep='last')

cols = [u'city', u'state', u'passengers']
tabs = tabs[cols]
tabs.set_index('city', inplace=True)

path = os.getcwd()
filename = '/data/airtraffic.csv'
file_path = path + filename
tabs.to_csv(file_path)
