from __future__ import division
import pandas as pd
import numpy as np
import quandl as ql
from StringIO import StringIO
from zipfile import ZipFile
from urllib import urlopen
import os

# get API key from environ
quandl_api_key = os.environ['QUANDL_API_KEY']

# def function to grab filenames from quandl database(s)
def get_file_metadata(zip_url):
    '''INPUT: url of zip file
       OUTPUT: list of lines from each file in zip file
       From Quandl output will be of the form:
       [[quandl file code 0, target file name 0],
       [quandl file code 1, target file name 1], ]
       '''
    file_list = []
    zipfile = ZipFile(StringIO(urlopen(zip_url).read()))
    names = zipfile.namelist()
    for name in names:
        for line in zipfile.open(name).readlines():
            file_list.append(line.strip('\n').split(','))
    return file_list
# list comp ^^
# file_list = [line for name in names for line in zipfile.open(name).readlines()...]

def get_files(file_names, target_directory_name):
    '''INPUT: list of file names, target directory name
       OUTPUT: csv files of passed names in target directory
    '''
    path = os.getcwd()+'/{}/'.format(target_directory_name)
    ql.ApiConfig.api_key = quandl_api_key

    if not os.path.exists(path):
        os.makedirs(path)

    for file_name in file_names:
        fixed_file_name = file_name[1].lower().replace(' - ', '_').replace(' ', '_')
        file_path = '{}{}{}'.format(path, fixed_file_name, '.csv')
        if not os.path.isfile(file_path):
            ql.get(file_name[0]).to_csv(file_path)

def quandl_data(lst):
    for url in urls:
        file_names, dir_prefix = get_file_metadata(url)
        get_files(file_names, dir_prefix, 'data/')

if __name__ == '__main__':
    urls = ['https://www.quandl.com/api/v3/databases/NVCA/codes',
'https://www.quandl.com/api/v3/databases/RENCAP/codes',
'https://www.quandl.com/api/v3/databases/CVR/codes',
'https://www.quandl.com/api/v3/databases/COOLEY/codes']

    quandl_data(urls)
