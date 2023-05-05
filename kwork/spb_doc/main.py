import requests
import lxml
import csv
from bs4 import BeautifulSoup

def pars_data(url):
    res = requests.get(url=url)
    res.encoding = 'utf-8'
    soup = BeautifulSoup(res.text, 'lxml')
    return soup

def main():
    with open('res.csv', 'w', encoding='utf-8-sig', newline='') as file:
        writer = csv.writer(file, delimiter=';')
        writer.writerow([
            'Сеть', 'Категория', 'Официальное название', 'Главный врач', 'Общая информация', 'Сайт', 'Телефон', 'Вконтакте', 'Одноклассники', 'Ютуб'])
    shema = 'https://doctu.ru'
    for i in range(1, 385):
        print(f'Итерация: {i}')
        soup = pars_data(f'https://doctu.ru/spb/clinics?page={i}')
        href_cards =[shema + i.find('a').get('href') for i in soup.find_all('div', class_='name')]

        for href_card in href_cards:
            soup = pars_data(href_card)
            try:
                network_clinics = soup.find('div', text='Сеть').next_sibling.find('a').text
            except Exception:
                network_clinics = 'Данных нет'
            try:
                cat_clinics = soup.find('div', text='Категория').next_sibling.find('a').text
            except Exception:
                cat_clinics = 'Данных нет'

            try:
                official_name = soup.find('div', text='Официальное название').next_sibling.text
            except Exception:
                official_name = 'Данных нет'

            try:
                name_doc = soup.find('div', text='Главный врач').next_sibling.text
            except Exception:
                name_doc = 'Данных нет'

            try:
                desc = soup.find('div', text='Общая информация').next_sibling.text
            except Exception:
                desc = 'Данных нет'

            try:
                website = shema + soup.find('div', class_='buttons').find('a', class_='btn btn-primary site').get('href')
            except Exception:
                website = 'Данных нет'

            try:
                tel = soup.find('div', class_='buttons').find('span').text
            except Exception:
                tel = 'Данных нет'

            try:
                vk_link = shema + soup.find('i', class_='fa fa-vk fa-fw').parent.get('href')
            except Exception:
                vk_link = 'Данных нет'

            try:
                ok_link = shema + soup.find('i', class_='fa fa-odnoklassniki fa-fw').parent.get('href')
            except Exception:
                ok_link = 'Данных нет'
            try:
                you_link = shema + soup.find('i', class_='fa fa-youtube-play fa-fw').parent.get('href')
            except Exception:
                you_link = 'Данных нет'

            flatten = network_clinics, cat_clinics, official_name, name_doc,  desc,  website, tel, vk_link, ok_link, you_link

            file = open('res.csv', 'a', encoding='utf-8-sig', newline='')
            writer = csv.writer(file, delimiter=';')
            writer.writerow(flatten)

    file.close()



if __name__ == '__main__':
    main()