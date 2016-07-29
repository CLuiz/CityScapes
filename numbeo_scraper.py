import requests
from bs4 import BeautifulSoup
import pandas as pd
import numpy as np
import os

def get_pages(url):
    '''
    INPUT: Target url for scraping with requests and bs4
    OUTPUT: List of raw soup objects
    '''
    # check compatibility with main for list vs single url input and output
    doc=requests.get(url).text
    soup = BeautifulSoup(doc, 'lxml')
    soup_can.append(soup)
    return soup_can

def build_urls(year_list):
    '''
    INPUT: List of years in form '20XX'
    OUTPUT: Url's ready to feed into the get_pages function
    '''
    return [url_prefix + year + url_suffix for year in year_list]

def clean_up(soup):
    '''
    INPUT: Fresh bs4 soup object
    OUTPUT: Stripped data text of interest from soup object
    '''
    data = []
    tab = soup.findAll('tbody')
    for t in tab:
        for tag in t.select('td'):
            data.append(tag.text)
    return data

def build_data_frames(zipped, chunk=8):
    '''
    INPUT: Tuple of form (year, table)
    OUTPUT: Dict in form of {year: DataFrame}
    '''
    df_dict ={}
    for item in zipped:
        df_dict[item[0]] = pd.DataFrame([list(entry) for entry in zip(*[iter(item[1])]*chunk)])
    return df_dict

        #return dict of df's with years as keys

def df_to_csv(dict_of_dataframes, target_directory_name='data', dir_prefix='Numbeo_cost_of_living'):
    '''
    INPUT: Output of build_data_frames function
    OUTPUT: Csv files of dataframes in:     ~/target_directory_name/dir_prefix/filename(default is year)
    '''
    path = os.getcwd()+'/{}/{}/'.format(target_directory_name, dir_prefix)

    if not os.path.exists(path):
        os.makedirs(path)
    for key, item in dict_of_dataframes.iteritems():
        file_path = '{}/{}.csv'.format(path, key)
        if not os.path.isfile(file_path):
            dict_of_dataframes[key].to_csv(file_path)

def fix_em(columns):
    '''
    INPUT: List of columns
    OUTPUT: Fixed list of columns
    '''
    fixed_columns =[]
    for column in columns:
        column = column.lower().replace(' ', '_')
        fixed_columns.append(column)
    return fixed_columns

def clean_up_df(df):
    '''
    INPUT: Dirty, dirty numbeo dataframe
    OUTPUT: DataFrame with cleaned column text
    '''
    df['state'] = df['city'].apply(lambda x: x.split(',')[1].strip().lower().replace(' ', '_'))
    df['city'] = df['city'].apply(lambda x: x.split(',')[0].lower().replace(' ', '_'))
    del df['rank']
    return df

def merger(df1, df2):
        '''
        INPUT: Two will enter...
        OUTPUT: One will leave...
        '''
    df_merge = pd.merge(df1, df2,
              left_on=['city', 'state'],
              right_on=['city', 'state'],
              how='outer')
    return df_merge

# global vars:

url_prefix = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title='
url_suffix = '&region=021'
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']
soup_can = []
table_list =[]


def main():
    # fix me, I'm fugly
    urls = build_urls(year_list)
    for url in urls:
        soup_can = get_pages(url)
    table_list = [clean_up(soup) for soup in soup_can]
    zipped = list(zip(year_list, table_list))
    df_dict = build_data_frames(zipped)
    columns= ['Rank','City','Cost of Living Index','Rent Index','Cost of Living Plus Rent Index','Groceries Index','Restaurant Price Index','Local Purchasing Power Index']
    columns = fix_em(columns)
    for item in year_list:
        columns= fix_em(['Rank','City','Cost of Living Index','Rent Index','Cost of Living Plus Rent Index', 'Groceries Index','Restaurant Price Index','Local Purchasing Power Index'])
        first_cols = columns[:2]
        first_cols.extend([column + '_{}'.format(item)for column in columns[2:]])
        df_dict[item].columns = first_cols

    df_2009 = clean_up_df(df_dict['2009'])
    df_2010 = clean_up_df(df_dict['2010'])
    df_2011 = clean_up_df(df_dict['2011'])
    df_2012 = clean_up_df(df_dict['2012'])
    df_2013 = clean_up_df(df_dict['2013'])
    df_2014 = clean_up_df(df_dict['2014'])
    df_2015 = clean_up_df(df_dict['2015'])
    df_2016 = clean_up_df(df_dict['2016'])

    df_list = [df_2009, df_2010,df_2011,df_2012, df_2013,df_2014,df_2015,df_2016]

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
    merged7.to_csv('data/Numbeo_cost_of_living/numbeo_complete.csv')
# TO DO
    # pull headers out of soup object


if __name__ == '__main__':
    main()
