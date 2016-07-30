import requests
from bs4 import BeautifulSoup
from numbeo_scraper import clean_up
import pandas as pd


def get_walk_data(ulr):
    doc = requests.get(url).text
    soup = BeautifulSoup(doc, 'lxml')
    return = clean_up(soup)

def data_framify(walk_data):
    # break into list of lists containing city:info
    chunked= [walk_data[x:x+6] for x in xrange(0, len(walk_data), 6)]
    # remove AU and CA cities
    chunked1 =chunked[:88]
    chunked2 = chunked[114:]
    chunked1.extend(chunked2)

    cols = ['city', 'state', 'walk_score', 'transit_score', 'bike_score', 'walk_pop']
    walk_df = pd.DataFrame(chunked1, columns=cols)
    walk_df.replace('--', -1, inplace=True)
    walk_df['state'] = walk_df['state'].apply(lambda x: x.lower())
    walk_df['city'] = walk_df['city'].apply(lambda x: x.lower().replace(' ', '_').replace('-', '_').replace('.', ''))

    walk_df['city'] = [item.replace('boise_city', 'boise') for item in walk_df['city']]
    # save this as  a csv for later
    return walk_df
# check wdc, louisville, north lv, boise, vBeach, st.louis, lexington, st.pete, jersey city, winston-salem

if __name__ == '__main__':
    url = 'https://www.walkscore.com/cities-and-neighborhoods/'
    walk_data = get_walk_data(url)
    # strip off Australian cities:
    walk_data = walk_data[:-42]
    walk_df = data_framify(walk_data)