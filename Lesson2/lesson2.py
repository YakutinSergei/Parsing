import requests
import json
from bs4 import BeautifulSoup

# url = "http://health-diet.ru/table_calorie/?utm_source=leftMenu&utm_medium=table_calorie"
#
# headers = {
#
# }
#
# req = requests.get(url)
#
#
# src = req.text
# #print(src)
# with open("index.html", "w") as file:
#     file.write(src)

# with open("index.html") as file:
#     src = file.read()
#
# soup = BeautifulSoup(src, "lxml")
# all_products_href = soup.find_all(class_="mzr-tc-group-item-href")
#
# all_categories_dict = {}
# for item in all_products_href:
#     item_text = item.text
#     item_href = "http://health-diet.ru" + item.get("href")
#
#     all_categories_dict[item_text] = item_href
#
# with open("all_categories_dict.json", "w") as file:  #Сохраняем в формате json
#     json.dump(all_categories_dict, file, indent=4, ensure_ascii=False)

with open("all_categories_dict.json") as file:
    all_categories = json.load(file)

print(all_categories)

