import requests
from bs4 import BeautifulSoup
import pandas as pd
import numbeo_scraper as ns

'''
todo:
-code:
--build url list from cities
--use numbeo scraper functions to clean up
--strip leading comma
--send nearly created csv files to the data folder
--turn this script into a function, then into a bigest us cities scraping object that takes a url and returns a cleaned csv file
-data:
-transform city names to the appropriate form
'''
url_prefix = 'https://www.biggestuscities.com/city/'

url ='https://www.biggestuscities.com/city/denver-colorado'

# response = requests.get(url)
# soup = BeautifulSoup(response.content, 'lxml')
soup = ns.get_pages(url)
tabs =[]
table = soup[0].findAll('table')

for tag in table:
    tabs.append(tag.text)


data =[t.replace("\n",",").strip() for t in tabs][-1].split(',,')[1:-1]
file_name = url.split('/')[-1].replace('-', '_')

pd.DataFrame(data).to_csv(file_name)

# Scrape the top 100 cities education info:
# above code works out of the box, just swap url

# url = 'https://www.biggestuscities.com/demographics/us/education-college-graduates-by-top-100-city'

d = [t.replace("\n",",").strip() for t in tabs][-1]
d = d.split(' ')
t = [item for item in d if item != '']
t_done = [item.replace(',',' ').strip()  for item in t]

just_table = t_done[4:]
chunks = [just_table[x:x+5] for x in xrange(0, len(just_table), 5)]
df = pd.DataFrame(chunks)
df.columns = ['rank', 'city', 'state', 'pct_college_grads']
file_name = url.split('/')[-1].replace('-', '_')

df.to_csv('file_name')
'''
More urls to scrape:
https://www.biggestuscities.com/demographics/us/people-foreign-born-by-top-100-city
https://www.biggestuscities.com/demographics/us/population-density-by-top-100-city
https://www.biggestuscities.com/demographics/us/income-per-household-by-top-100-city
https://www.biggestuscities.com/demographics/us/business-retail-sales-per-capita-by-top-100-city
https://www.biggestuscities.com/demographics/us/business-total-businesses-by-top-100-city
'''
