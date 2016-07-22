import requests
from bs4 import BeautifulSoup
import re




url = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title=2016&region=021'

doc=requests.get(url).text

soup = BeautifulSoup(doc)

print soup.prettify()
