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
    result_json= []

    for href_category in href_categories:
        soup = get_data(href_category)
        href_pages = [f"{shema}{link['href']}" for link in soup.find('div', class_='pagen').find_all('a')]
        for href_page in href_pages:
            soup = get_data(href_page)
            href_cards = href_pages = [f"{shema}{link['href']}" for link in
                                       soup.find('div', class_='item_card').find_all('a', class_='name_item')]

            for href_card in href_cards:
                soup = get_data(href_card)
                name = [x.text.strip() for x in soup.find_all('p', id='p_header')]
                article = [x.text.split(':')[-1].strip() for x in soup.find_all('p', class_='article')][0]
                description = [x.text.strip().split('\n') for x in soup.find_all('ul', id='description')]
                count = [x.text.split(':')[-1].strip() for x in soup.find_all('span', id='in_stock')]
                price = [x.text for x in soup.find_all('span', id='price')]
                old_price = [x.text for x in soup.find_all('span', id='old_price')]
                description_li = [soup.find('ul', id='description').find_all('li')]
                category = [href_card.split('/')[4].strip()]

                for category, list_item, price_item, name, count, price, old_price, li_desc in zip(category, description, price, name, count,
                                                                                         price, old_price, description_li):
                    result_json.append({
                        'categories': category,
                        'name': name,
                        'article': article,
                        'description ': {
                            [x['id'] for x in li_desc][0]: [x.split(':')[-1] for x in list_item][0],
                            [x['id'] for x in li_desc][1]: [x.split(':')[-1] for x in list_item][1],
                            [x['id'] for x in li_desc][2]: [x.split(':')[-1] for x in list_item][2],
                            [x['id'] for x in li_desc][3]: [x.split(':')[-1] for x in list_item][3],
                            [x['id'] for x in li_desc][4]: [x.split(':')[-1] for x in list_item][4],
                            [x['id'] for x in li_desc][5]: [x.split(':')[-1] for x in list_item][5],
                            [x['id'] for x in li_desc][6]: [x.split(':')[-1] for x in list_item][6],
                            [x['id'] for x in li_desc][7]: [x.split(':')[-1] for x in list_item][7],
                        },
                        'count': count,
                        'price': price_item,
                        'old_price': old_price,
                        'link': href_card
                    })
    with open('res.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)


if __name__ == "__main__":
    main()