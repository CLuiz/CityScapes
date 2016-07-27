from __future__ import unicode_literals
import requests
import json
import time
import codecs
import sys
import os

UTF8Writer = codecs.getwriter('utf8')
sys.stdout = UTF8Writer(sys.stdout)

def main():
        cities =[("Denver","CO"),("Boulder","CO")]
        api_key= os.environ['MEETUP_API_KEY']

        for (city, state) in cities:
            per_page = 200
            results_we_got = per_page
            offset = 0

            while (results_we_got == per_page):
                response=get_results({"sign":"true","country":"US", "city":city, "state":state, "radius": 10, "key":api_key, "page":per_page, "offset":offset })
                time.sleep(1)
                offset += 1
                results_we_got = response['meta']['count']
                for group in response['results']:
                    category = ""
                    if "category" in group:
                        category = group['category']['name']
                    print "," .join(map(unicode, [city, group['name'].replace(","," "), group['created'], group['city'],group.get('state',""),category,group['members'], group.get('who',"").replace(","," ")]))

            time.sleep(1)


def get_results(params):
    request = requests.get("http://api.meetup.com/2/groups",params=params)
    data = request.json()
    return data

if __name__=="__main__":
        main()
