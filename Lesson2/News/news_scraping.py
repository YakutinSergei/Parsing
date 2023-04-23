import requests
import json
import  csv
from bs4 import BeautifulSoup
from datetime import datetime

headers = {
    "user-agent": "Mozilla/5.0 (X11; Linux x86_64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/110.0.0.0 YaBrowser/23.3.1.906 (beta) Yowser/2.5 Safari/537.36"
}


words = ["Химическое", "Биологическое", "дили"]

news = {}


now = datetime.now()
current_time = now.strftime("%H:%M")
times = now.strftime("%H")+now.strftime("%M")
print(times)

last_time = 0

while True:
    url = f"https://ria.ru/services/archive/widget/more.html?id=1867145539&date=20230423T{times}40&articlemask=lenta_common&type=lenta"
    req = requests.get(url)
    src = req.text

    with open(f"data/{times}.html", "w") as file: #Записываем данные в файл
        file.write(src)

    with open(f"data/{times}.html") as file: #Открываем файл
        src = file.read()

    soup = BeautifulSoup(src, "lxml")
    all_news = soup.find_all(class_="lenta__item-size")


    for item in all_news:
        news_href = "https://ria.ru"+item.get("href")
        news_disc = item.text[5:]

        news[news_href] = [news_disc, item.text[:5]]

        for word in words:
            if word.lower() in news_disc.lower():
                #print(item.text)
                news_href = soup.find("span", string=item.text)

                break




    if int(last_time) < int(times):
        break
    break
#print(url)
print(news['https://ria.ru/20230423/zamorozki-1867168471.html'][1])
