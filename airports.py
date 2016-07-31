import pandas as pd


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
# todo get these values updated!!!11!!!1!1


# account for multi-city airports
baltimore = fixed_washington
newark = fixed_new_york
fort_worth = fixed_dallas
tacoma = tabs.loc[tabs['city'] == 'seattle']
tacoma['city'] = 'tacoma'
st_paul = tabs.loc[tabs['city'] == 'minneapolis']
st_paul['city'] = 'st_paul'
durham = tabs.loc[tabs['city'] == 'raleigh']
durham['city'] = 'durham'

# add duplicated city rows
add_cities = [tacoma, st_paul, durham]
tabs = tabs.append(add_cities)
