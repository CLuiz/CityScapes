import requests
from bs4 import BeautifulSoup
import re


# fix me

url = 'http://www.census.gov/data/datasets/1997/econ/susb/1997-susb.html'

doc=requests.get(url).text

soup = BeautifulSoup(doc)

print soup.prettify()

soup_links = soup.findAll('a', href=re.compile('^www2.census.gov/programs-surveys/susb/datasets/1997'))

links = re.findall("www2.census.gov/programs-surveys/susb/datasets/1997", str(doc))














# http://www2.census.gov/programs-surveys/susb/datasets/1997/msa_2digitsic_1997.txt
#
# http://www2.census.gov/programs-surveys/susb/datasets/1997/us_state_4digitsic_1997.txt
# http://www2.census.gov/programs-surveys/susb/datasets/1997/us_state_sicmajorindustry_detailedsizes_1997.txt
#
#
# http://www.census.gov/data/datasets/2012/econ/susb/2012-susb.html
#
# http://www2.census.gov/programs-surveys/susb/datasets/2012/us_state_6digitnaics_2012.txt
#
# http://www2.census.gov/programs-surveys/susb/datasets/2012/us_state_naics_detailedsizes_2012.txt
