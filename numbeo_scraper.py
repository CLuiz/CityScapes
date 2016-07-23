import requests
from bs4 import BeautifulSoup

soup_can = []
def get_pages(url):
    doc=requests.get(url).text
    soup = BeautifulSoup(doc, 'lxml')
    soup_can.append(soup)
    return soup_can

def build_urls(year_list):
    url_list = []
    for year in year_list:
        url = url_prefix + year + url_suffix
        url_list.append(url)
    return url_list

# integrate this next:
def clean_up(soup):
    data = []
    tab = soup.findAll('tbody')
    for t in tab:
        for tag in t.select('td'):
            data.append(tag.text)
    return data

    # This could be the missing piece:
#df = pd.DataFrame([sub.split(",") for sub in l])

url_prefix = 'http://www.numbeo.com/cost-of-living/region_rankings.jsp?title='
url_suffix = '&region=021'
year_list = ['2009', '2010', '2011', '2012', '2013', '2014', '2015', '2016']



if __name__ == '__main__':
    urls = build_urls(year_list)
    table_list =[]

    for url in urls:
        soup_can = get_pages(url)

    for soup in soup_can:
        table_list.append(clean_up(soup))

    zipped = list(zip(year_list, table_list))
