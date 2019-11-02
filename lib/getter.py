import re
import json
import urllib.request
import urllib.parse


URL = 'https://d3.ru/api/feed/?'


def get_data(params=dict(page=1, feed_type='all', sorting='hotness')):
    params_encoded = urllib.parse.urlencode(params)
    api_url = f'{URL}{params_encoded}'
    res_body = get_responce(api_url)
    data = json.loads(res_body.decode('utf-8'))
    return data


def get_responce(url):
    res = urllib.request.urlopen(url)
    return res.read()

