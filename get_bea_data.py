import pandas as pd

url = 'http://www.bea.gov/newsreleases/regional/gdp_metro/2015/xls/gdp_metro0915.xls'
f = pd.DataFrame(pd.read_excel(url))
f.to_csv('/Users/IXChris/Desktop/G/capstone/data/bea.csv')
