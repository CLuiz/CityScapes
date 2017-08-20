import os

from bs4 import BeautifulSoup
import pandas as pd
import requests


def run_me():
    df1 = pd.read_csv('data/biggestuscities/business_retail_sales_per_capita_by_top_100_city.csv')
    df1['city'] = df1['city'].apply(lambda x: x.replace('_', '-'))
    df1['state_rs'] = df1['state_rs'].apply(lambda x: x.replace('_', '-'))
    df1['combo'] = df1['city'] + '-' + df1['state_rs']
    city_list = list(df1['combo'])
    #city_list = ['cleveland-ohio', 'atlanta-georgia', ]
    for city in city_list:
        url_suffix = city
        url_prefix = 'https://www.biggestuscities.com/city/'
        url = url_prefix + url_suffix
        path = os.getcwd() + '/data/biggestuscities'
        file_name = url.split('/')[-1].replace('-', '_')
        file_path = '{}/{}.csv'.format(path, file_name)
        doc = requests.get(url)
        if doc.content != 'Not Found!':
            soup = BeautifulSoup(doc.content, 'lxml')
            table = soup.findAll('table')
            # print table
            tabs = [tag.text for tag in table]
            # print tabs
            data = [t.replace("\n",",").strip() for t in tabs][-1].split(',,')[1:-1]
            # print data
            data = [item[1:].split(',') for item in data if item]
            dd = pd.DataFrame(data)[1:6]
            dd['pop'] = dd[1]+dd[2]
            da = pd.DataFrame(zip(dd[0], dd['pop']))
            done = da.T
    return done
