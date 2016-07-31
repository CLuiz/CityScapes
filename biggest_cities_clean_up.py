import pandas as pd
import os

local_path = os.getcwd()
file_path= '/data/biggestuscities/business_retail_sales_per_capita_by_top_100_city.csv'
path = local_path + file_path
retail_df = pd.read_csv(path)
cols = [u'city', u'retail_sales']
retail_df = retail_df[cols]
retail_df['retail_sales'] = retail_df['retail_sales'].map(lambda x: float(x.replace(' ','')))


replace_dict = {'paul': 'st_paul',
                'jose': 'san_jose',
                'kansas': 'kansas_city',
                'lexington-fayette': 'lexington',
                'long': 'long_beach',
                'louis': 'st_louis',
                'louisville/jefferson': 'louisville',
                'nashville-davidson': 'nashville',
                'oklahoma': 'oklahoma_city',
                'paso': 'el_paso',
                'paul': 'st_paul',
                'petersburg': 'st_petersburg',
                'winston-salem': 'winston_salem',
                'bernadino': 'san_bernadino',
                'colorado': 'colorado_springs',
                'new_jersey': 'jersey_city'
}
