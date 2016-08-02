import pandas as pd
import os

def cleaner(df, target_column):
    cols = [u'city', target_column]
    df = df[cols]
    df[target_column] = df[target_column].map(lambda x: x.replace(' ',''))
    df = df.replace(replace_dict)
    return df

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
                'bernardino': 'san_bernardino',
                'colorado': 'colorado_springs',
                'new_jersey': 'jersey_city',
                'corpus': 'corpus_christi',
                'angeles': 'los_angeles',
                'chesapeake': 'chesapeake_bay'
}

# pop_density data first
local_path = os.getcwd()
file_path= '/data/biggestuscities/population_density_by_top_100_city.csv'
path = local_path + file_path
pop_density_df = pd.read_csv(path)
pop_density_df = cleaner(pop_density_df, 'pop_density')
# clean up cols to match master df values
# this is population density info!
cols = [u'city', u'pop_density']
pop_density_df = pop_density_df[cols]
pop_density_df['pop_density'] = pop_density_df['pop_density'].map(lambda x: float(x.replace(' ','')))

# Data is wrong need to check scraper
# combine vegas and north vegas:
fixed_vegas = pop_density_df.loc[pop_density_df['city'] == 'las_vegas', 'pop_density'].sum()
# pop_density_df = pop_density_df.(_dict)
pop_density_df.set_index('city', inplace=True)
pop_density_df.set_value('las_vegas', 'pop_density', fixed_vegas)
pop_density_df.reset_index(inplace=True)
pop_density_df = pop_density_df.drop_duplicates(subset='city', keep='last')
pop_density_df.set_index('city', inplace=True)

new_file_path = '/data/biggestuscities/clean_pop_density.csv'
path = local_path + new_file_path
pop_density_df.to_csv(path)

# now total businesses
# THIS DATA IS WRONG  NEED TO RE_SCRAPE
# file_path= '/data/biggestuscities/business_total_businesses_by_top_100_city.csv'
# path = local_path + file_path
# total_businesses_df = pd.read_csv(path)
#
def cleaner(df, target_column):
    cols = [u'city', target_column]
    df = df[cols]
    df[target_column] = df[target_column].map(lambda x: x.replace(' ',''))
    df = df.replace(replace_dict)
    return df

# business_df = cleaner(total_businesses_df, 'total_businesses')
# new_file_path = '/data/biggestuscities/clean_total_business.csv'
# path = local_path + new_file_path
# business_df.to_csv(path)


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

#foreign born by city
file_path = '/data/biggestuscities/people_foreign_born_by_top_100_city.csv'
path = local_path + file_path
foreign_df = pd.read_csv(path)
foreign_df = cleaner(foreign_df, 'pct_foreign_born')
foreign_df['pct_foreign_born'] = foreign_df['pct_foreign_born'].map(lambda x: float(x.replace('%', '')))
foreign_df = foreign_df.drop_duplicates(subset='city', keep='first')
foreign_df.set_index('city', inplace=True)

new_file_path = '/data/biggestuscities/clean_foreign_born.csv'
path = local_path + new_file_path
foreign_df.to_csv(path)
