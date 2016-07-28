import big_us_cities_scraper as bs

url = 'https://www.biggestuscities.com/demographics/us/education-college-graduates-by-top-100-city'

cols = ['rank', 'city','state_bc','pct_college_grads_bc']
grad_df = bs.get_grad_data(url, cols)

url1 = 'https://www.biggestuscities.com/demographics/us/population-density-by-top-100-city'

cols1 = ['rank', 'city','state_de','pop_density']
density_df = bs.get_grad_data(url1, cols1, skip_rows=2)

url2 = 'https://www.biggestuscities.com/demographics/us/income-per-household-by-top-100-city'
cols2 = ['rank', 'city','state_iph','inc_per_household']

house_inc_df = bs.get_grad_data(url2, cols2, skip_rows=2)
house_inc_df['inc_per_household'] = house_inc_df['inc_per_household'].apply(lambda x: x.replace(' ', ''))


url3 ='https://www.biggestuscities.com/demographics/us/business-retail-sales-per-capita-by-top-100-city'

cols3 = ['rank', 'city','state_rs','retail_sales']
retail_sales_df = bs.get_grad_data(url3, cols3, skip_rows=2)
retail_sales_df['retail_sales'] = retail_sales_df['retail_sales'].apply(lambda x: x.replace(' ', ''))

url4 ='https://www.biggestuscities.com/demographics/us/business-total-businesses-by-top-100-city'
cols4 = ['rank', 'city','state_bs','total_businesses']
businesses_df = bs.get_grad_data(url4, cols4, skip_rows=2)
businesses_df['total_businesses'] = businesses_df['total_businesses'].apply(lambda x: x.replace(' ', ''))
