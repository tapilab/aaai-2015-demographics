"""
Scrape QuantCast demographic information. Ids read from file specified on command-line.

e.g.

$ cat /data/tweco/qcast_ids.txt
answers.com
$ python qcast.py /data/tweco/qcast_ids.txt
{"No Kids": 86, "$0-50k": 112, "45-54": 100, "$150k+": 74, "Other": 98, "55-64": 82, "Caucasian": 94, "< 18": 69, "No College": 92, "35-44": 104, "65+": 74, "$100-150k": 81, "Grad School": 84, "brand": "answers.com", "25-34": 111, "Hispanic": 127, "African American": 122, "Male": 87, "$50-100k": 94, "Has Kids": 115, "18-24": 152, "College": 115, "Asian": 97, "Female": 112}
"""
import json
import re
import requests
import sys
import time

from BeautifulSoup import BeautifulSoup as bs


def read_file(filename):
    return [l.strip() for l in open(filename, 'rb').readlines()]


url = 'https://www.quantcast.com/'
classes = ['tr-GENDER', 'tr-AGE', 'tr-CHILDREN', 'tr-INCOME', 'tr-EDUCATION', 'tr-ETHNICITY', 'tr-POLITICS']
brands = read_file(sys.argv[1])
for brand in brands:
    u = url + brand + '/demographics'
    data = {}
    data['brand'] = brand
    try:
        soup = bs(requests.get(u).text)
        for cl in soup.findAll(attrs={'class': 'demographics-composition'}):
            for tr in cl.findAll('tr'):
                label = tr.findChild(attrs={'style': 'text-align:left; padding-right:2px; width:108px'}).contents[0].strip()
                value = tr.findChild(attrs={'class': re.compile(r"index-digit.*")}).contents[0].strip()
                data[label] = value
        print json.dumps(data, sort_keys=True)
        time.sleep(1)  # Be nice and sleep 1 second between calls.
    except Exception as e:
        sys.stderr.write('exception %s, skipping\n' % e)
