import requests

import json

from bs4 import BeautifulSoup

url = 'https://parsinger.ru/html/index1_page_1.html'

schema = 'https://parsinger.ru/html/'


def make_soup(url, encoding='utf-8'):
    r = requests.get(url)

    r.encoding = encoding

    soup = BeautifulSoup(r.text, 'lxml')

    return soup


def find_a(soup, class_name=None):
    '''

    finding link from all tags <a>

    '''

    return [a['href'] for a in soup.find('div', class_=class_name).find_all('a')]


result_list = []

main_soup = make_soup(url)

categories = find_a(main_soup, 'nav_menu')

for category in categories:

    category_page = schema + category

    category_soup = make_soup(category_page)

    pages = find_a(main_soup, 'pagen')

    for page in pages:

        items_page = schema + page

        items_soup = make_soup(items_page)

        name = [a.text.strip() for a in items_soup.find_all('a', class_='name_item')]

        description = [div.text.strip().split('\n') for div in items_soup.find_all('div', class_='description')]

        price = [p.text for p in items_soup.find_all('p', class_='price')]

        for name, descr, price in zip(name, description, price):
            result_list.append(

                {'Название': name,

                 **{k.strip(): v.strip() for k, v in [d.split(':') for d in descr]},

                 'Цена': price})

with open('result_all_categories.json', 'w') as f:
    json.dump(result_list, f, indent=4, ensure_ascii=False)