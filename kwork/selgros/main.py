import requests
import json
import csv
import lxml
from bs4 import BeautifulSoup
from fake_useragent import UserAgent

ua = UserAgent()
fake_ua = {'user-agent': ua.random}

url = 'https://delivery.selgros.ru/?_ga=2.148258804.259091941.1683628801-1503554812.1683628801&_gl=1*dys9cq*_ga*MTUwMzU1NDgxMi4xNjgzNjI4ODAx*_ga_G6K2HYN39V*MTY4MzYyODgwMC4xLjAuMTY4MzYyODgwMC42MC4wLjA.'

def pars_data(url):
    res = requests.get(url=url, headers=fake_ua)
    res.encoding='utf-8'
    return BeautifulSoup(res.text, 'lxml')

def main():
    soup = pars_data(url)
    print(soup)

if __name__ == '__main__':
    main()