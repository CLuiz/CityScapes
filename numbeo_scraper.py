import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

def get_pages(url):
    doc=requests.get(url).text
    soup = BeautifulSoup(doc, 'lxml')
    soup_can.append(soup)
    return soup_can

def build_urls(year_list):
    url_list = []
    for year in year_list:
        url = url_prefix + year + url_suffix
        url_list.append(url)
    return url_list

# integrate this next:
def clean_up(soup):
    data = []
    tab = soup.findAll('tbody')
    for t in tab:
        for tag in t.select('td'):
            data.append(tag.text)
    return data

def build_data_frames(zipped, chunk=8):
    '''INPUT: Tuple of form (year, table)
       OUTPUT: Dict in form of {year: DataFrame}
    '''
    df_dict ={}
    for item in zipped:
        df_dict[item[0]] = pd.DataFrame([list(entry) for entry in zip(*[iter(item[1])]*chunk)])
    return df_dict

        #return dict of df's with years as keys

def df_to_csv(dict_of_dataframes, target_directory_name='data', dir_prefix='Numbeo_cost_of_living'):
    '''INPUT: Output of build_data_frames function
       OUTPUT: Csv files of dataframes in ~/target_directory_name/dir_prefix/filename(default is year)
    '''
    path = os.getcwd()+'/{}/{}/'.format(target_directory_name, dir_prefix)

    if not os.path.exists(path):
        os.makedirs(path)
    for key, item in dict_of_dataframes.iteritems():
        file_path = '{}/{}.csv'.format(path, key)
        if not os.path.isfile(file_path):
            dict_of_dataframes[key].to_csv(file_path)

def fix_em(columns):
    '''INPUT: List of columns
       OUTPUT: Fixed list of columns
    '''
    fixed_columns =[]
    for column in columns:
        column = column.lower().replace(' ', '_')
        fixed_columns.append(column)
    return fixed_columns

# global vars:

url_prefix = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title='
url_suffix = '&region=021'
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
soup_can = []
table_list =[]


def main():
    urls = build_urls(year_list)
    for url in urls:
        soup_can = get_pages(url)
    for soup in soup_can:
        table_list.append(clean_up(soup))
    zipped = list(zip(year_list, table_list))
    df_dict = build_data_frames(zipped)
    columns= ['Rank','City','Cost of Living Index','Rent Index','Cost of Living Plus Rent Index','Groceries Index','Restaurant Price Index','Local Purchasing Power Index']
    for k, v in df_dict.iteritems():
        v.columns = fix_em(columns)
    df_to_csv(df_dict)

# TO DO
    # pull headers out of soup object


if __name__ == '__main__':
    main()
