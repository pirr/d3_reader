import re
import json
import urllib.request
import urllib.parse
from html.parser import HTMLParser



URL = 'https://d3.ru/api/feed/?'


class HTMLFilter(HTMLParser):
    text = ""

    def handle_starttag(self, tag, attrs):
        if tag in ('br', 'p'):
            self.text += '\n'

    def handle_data(self, data):
        self.text += data


def get_data(params=dict(page=1, feed_type='all', sorting='hotness')):
    params_encoded = urllib.parse.urlencode(params)
    api_url = f'{URL}{params_encoded}'
    res = urllib.request.urlopen(api_url)
    res_body = res.read()
    data = json.loads(res_body.decode('utf-8'))
    return data
