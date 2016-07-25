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
