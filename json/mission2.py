import requests
import lxml
import json

from bs4 import BeautifulSoup


def get_data(url):
    res = requests.get(url=url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    return soup


def main():
    soup = get_data('https://parsinger.ru/html/index1_page_1.html')
    shema = 'http://parsinger.ru/html/'
    href_categories = [f"{shema}{link['href']}" for link in soup.find('div', class_='nav_menu').find_all('a')]

    for href_category in href_categories:
        soup = get_data(href_category)
        href_pages = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]

        for href_page in href_pages:
            soup = get_data(href_page)
            name = [x.text.strip() for x in soup.find_all('a', class_='name_item')]
            description = [x.text.strip().split('\n') for x in soup.find_all('div', class_='description')]
            price = [x.text for x in soup.find_all('p', class_='price')]
            result_json = []
            for list_item, price_item, name in zip(description, price, name):
                result_json.append({
                    'name': name,
                    [x.split(':')[0] for x in list_item][0]: [x.split(':')[-1] for x in list_item][0],
                    [x.split(':')[0] for x in list_item][1]: [x.split(':')[-1] for x in list_item][1],
                    [x.split(':')[0] for x in list_item][2]: [x.split(':')[-1] for x in list_item][2],
                    [x.split(':')[0] for x in list_item][3]: [x.split(':')[-1] for x in list_item][3],
                    'price': price_item
                })
            with open('res.json', 'a', encoding='utf-8') as file:
                json.dump(result_json, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()