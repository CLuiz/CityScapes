import pandas as pd
import os

def get_bea_data(url):
    '''
    INPUT: target url of bea excel file
    OUTPUT: raw df to pass to cleaning function
    '''
    file_name = url.split('/')[-1].split('.')[0]
    path = os.getcwd()+'/data/BEA' #/{}'.format(file_name)
    file_path = '{}/{}.csv'.format(path, file_name)

    if not os.path.exists(path):
        os.makedirs(path)
    if not os.path.isfile(file_path):
        f = pd.DataFrame(pd.read_excel(url))
        f.to_csv(file_path)
    return pd.read_csv(file_path, header=2)


def clean_me(bea_df):
    '''
    INPUT: Bea dataframe from get_bea_data function
    OUTPUT: Clean dataframe ready for merge into main frame
    '''
    columns = bea_df.columns
    new_columns = [u'city', u'bea_state', u'bea_2009', u'bea_2010', u'bea_2011', u'bea_2012',
           u'bea_2013', u'bea_2014', u'bea_what_is_this _crap']
    bea_df.columns = new_columns
    bea_df['city'] = bea_df['bea_state'].apply(lambda x: x.split(',')[0])
    bea_df['city'] = bea_df['city'].apply(lambda x: x.lower().replace('-', '_').replace(' ', '_'))
    bea_df['bea_state'] = bea_df['bea_state'].apply(lambda x: x.split(',')[-1])
    bea_df.set_index('city', inplace=True)
    return bea_df

def main():
    url = 'http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls'
    bea_df = get_bea_data(url)
    return clean_me(bea_df)



if __name__ == '__main__':
    bea_df = main()
