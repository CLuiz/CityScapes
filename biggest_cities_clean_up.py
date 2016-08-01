import pandas as pd
import os


# retail data first
local_path = os.getcwd()
file_path= '/data/biggestuscities/business_retail_sales_per_capita_by_top_100_city.csv'
path = local_path + file_path
retail_df = pd.read_csv(path)

# clean up cols to match master df values
# this is population density info!
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
                'new_jersey': 'jersey_city',
                'corpus': 'corpus_christi'
}

# combine vegas and north vegas:
fixed_vegas = retail_df.loc[retail_df['city'] == 'las_vegas', 'retail_sales'].sum()
retail_df = retail_df.replace(replace_dict)
retail_df.set_index('city', inplace=True)
retail_df.set_value('las_vegas', 'retail_sales', fixed_vegas)
retail_df.reset_index(inplace=True)
retail_df = retail_df.drop_duplicates(subset='city', keep='last')
retail_df.set_index('city', inplace=True)

new_file_path = '/data/biggestuscities/clean_retail.csv'
path = local_path + new_file_path
retail_df.to_csv(path)

# now total businesses
# THIS DATA IS WRONG  NEED TO RE_SCRAPE
file_path= '/data/biggestuscities/business_total_businesses_by_top_100_city.csv'
path = local_path + file_path
total_businesses_df = pd.read_csv(path)

def cleaner(df, target_column):
    cols = [u'city', target_column]
    df = df[cols]
    df[target_column] = df[target_column].map(lambda x: x.replace(' ',''))
    df = df.replace(replace_dict)
    return df

business_df = cleaner(total_businesses_df, 'total_businesses')
new_file_path = '/data/biggestuscities/clean_total_business.csv'
path = local_path + new_file_path
business_df.to_csv(path)


# now graduates per city
file_path = '/data/biggestuscities/education_college_graduates_by_top_100_city.csv'
path = local_path + file_path
grad_df = pd.read_csv(path)

grad_df = cleaner(grad_df, 'pct_college_grads_bc')
grad_df['pct_college_grads_bc'] = grad_df['pct_college_grads_bc'].map(lambda x: float(x.replace('%', '')))
grad_df = grad_df.drop_duplicates(subset='city', keep='first')
grad_df.set_index('city', inplace=True)

new_file_path = '/data/biggestuscities/clean_grad.csv'
path = local_path + new_file_path
grad_df.to_csv(path)

#
 file_path = 'data/biggestuscities/income_per_household_by_top_100_city.csv'
 path = local_path + file_path
 income_df = pd.read_csv(path)

 income_df = cleaner(income_df, 'inc_per_household')
 income_df['inc_per_household'] = income['inc_per_household'].map(lambda x: float(x))
