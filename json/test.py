import json

import requests
from bs4 import BeautifulSoup
from fake_useragent import FakeUserAgent


headers = {
    'user-agent': FakeUserAgent().random
}

MAIN_URL = 'https://parsinger.ru/html/'

def write_json(data):

    result_json = []

    splitDescription = lambda text: text.split(':', 1)

    for pageProduks in data:
        for name, article, descriptio, in_stock, prices, url in pageProduks:
            result_json.append({
                'Название': name,
                'Артикул': article.split(': ')[-1],
                'Описание': {
                    splitDescription(item)[0]: splitDescription(item)[-1].lstrip() for item in descriptio
                },
                'В наличии': in_stock.split(': ')[-1],
                'Цена': prices[0],
                'Старая цена': prices[1],
                'url': url,
            })

    with open('result.json', 'w', encoding='utf-8') as file:
        json.dump(result_json, file, indent=4, ensure_ascii=False)

def makeSoup(url):
    response = requests.get(url=url, headers=headers)
    response.encoding = 'utf-8'

    soup = BeautifulSoup(response.text, 'lxml')

    return soup

def takeInfoProduks(navigation):
    infoProduct = []
    urlProducts = []

    pagen = [MAIN_URL + a['href'] for a in makeSoup(navigation).find('div', class_='pagen').find_all('a')]

    for page in pagen:
        urlProducts.extend([MAIN_URL + a['href'] for a in makeSoup(page).find_all('a', class_='name_item')])

    for urlProduct in urlProducts:
        soup = makeSoup(urlProduct)
        name = soup.find('p', id='p_header').text
        article = soup.find('p', class_='article').text
        descriptio = [li.text for li in soup.find('ul', id='description').find_all('li')]
        in_stock = soup.find('span', id='in_stock').text
        prices = [span.text for span in soup.find('div', class_='sale').find_all('span')]
        infoProduct.append([name, article, descriptio, in_stock, prices, urlProduct])

    return infoProduct

def main():
    url = 'https://parsinger.ru/html/index1_page_1.html'

    nav_menu = [MAIN_URL + a['href'] for a in makeSoup(url).find('div', class_='nav_menu').find_all('a')]
    productList = []

    for navigation in nav_menu:
        productList.append(takeInfoProduks(navigation))

    write_json(productList)

if __name__ == '__main__':
    main()