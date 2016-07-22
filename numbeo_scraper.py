import requests
from bs4 import BeautifulSoup

soup_can = []
def get_pages(url):
    doc=requests.get(url).text
    soup = BeautifulSoup(doc)
    soup_can.append(soup)
    return soup_can

def build_urls(year_list):
    url_list = []
    for year in year_list:
        url = url_prefix + year + url_suffix
        url_list.append(url)
    return url_list

url_prefix = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title='
url_suffix = '&region=021'
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']



if __name__ == '__main__':
    urls = build_urls(year_list)

    for url in urls:
        get_pages(url)
