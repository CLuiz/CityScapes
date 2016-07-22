import meetup.api as ma
import json
import os
import requests

api_key = os.environ=['MEETUP_API_KEY']

client = ma.Client(api_key)

# city = 'Denver'
# topic = None

# def getEvent(url_path, key) :
#     responseString = ""
#
#     params = {'city':city, 'key':key,'topic':topic}
#     r = requests.get(url_path, params = params)
#     print(r.url)
#     responseString = r.text
#     return responseString
#
cities =[("Bridgeport","CT"),("New Haven","CT"),("Hartford","CT"),("Stamford","CT"),("Waterbury","CT")]

for (city, state) in cities:
    per_page = 200
    results_we_got = per_page
    offset = 0
    while (results_we_got == per_page):
        # Meetup.com documentation here: http://www.meetup.com/meetup_api/docs/2/groups/
        # You can change search perimeter around each city by changing the "radius" parameter
        response=get_results({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page, "offset":offset })
        time.sleep(1)
        offset += 1
        #results_we_got = response['meta']['count']
        #print results_we_got
