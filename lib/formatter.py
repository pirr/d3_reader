from io import BytesIO
from typing import List
from html.parser import HTMLParser
from lib.reader import covertImageToAscii
from lib.getter import get_responce


class Article(object):
    """
    Class for create article from d3 post
    """
    
    def __init__(self, _id: int = None, title: str = None, text: str = None, image_url: str = None, link: str = None, rating: int = None):
        self.id = _id
        self.title = title
        self.text = text
        self.image_url = image_url
        self.link = link
        self.rating = rating
    
    @staticmethod
    def _populate_html(html_text):
        """
        Clear html tags, convert to new line 
        """
        parser = HTMLFilter()
        parser.feed(html_text)
        return parser.text

    def print_text(self):
        """
        Print article text
        """
        if self.text:
            text = self._populate_html(self.text)
            print(text)

    def print_title(self):
        """
        Print title text
        """
        if self.title:
            print(self.title.upper())

    def print_image(self):
        """
        Print image as ascii text
        """
        if self.image_url:
            img_bytes = get_responce(self.image_url)
            img_row_ascii = covertImageToAscii(BytesIO(img_bytes), cols=80, scale=0.6, moreLevels=False)
            print('\n'.join(img_row_ascii))

    def print_rating(self):
        """
        Print rating
        """
        if self.rating:
            print(self.rating)

    def print_link(self):
        """
        Print url link
        """
        if self.link:
            print(self.link)

    def show(self):
        """
        Print article
        """
        print('-' * 15, '*' * 3, '-' * 15)
        self.print_title()
        self.print_text()
        self.print_image()
        self.print_rating()
        self.print_link()
        print('=' * 33)

    def from_json(self, json_data):
        """
        Set attributes from JSON data
        """
        self.id = json_data['id']
        self.title = json_data['title']
        if json_data['data']['text']:
            self.text = json_data['data']['text']
        if 'main_image_url' in json_data:
            self.image_url = json_data['main_image_url']
        if 'rating' in json_data and json_data['rating']:
            self.rating = int(json_data['rating'])
        self.link = json_data['_links'][1]['href']


class HTMLFilter(HTMLParser):
    """
    HTML filter for convert html to text
    """

    text = ''

    def handle_starttag(self, tag, attrs):
        if tag in ('br', 'p'):
            self.text += '\n'

    def handle_data(self, data):
        self.text += data
    