import requests
from bs4 import BeautifulSoup

url = "https://rozetka.com.ua/ua/notebooks/c80004/sort=rank/"
user_agent = {
    "Accept": "text/html",
    "User-Agent": "Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/125.0.0.0 Safari/537.36 Edg/125.0.0.0",
}

get_page = requests.get(url, headers=user_agent)
get_content = get_page.text
soup_obj = BeautifulSoup(get_content, "html.parser")
find_content = soup_obj.find_all("div", class_="goods-tile__content")
product_list = []
for product in find_content:
    product_param = [
        (str(item)).replace("\xa0", ".")
        for item in product.stripped_strings
        if len(item) > 1 and item != "Готовий до відправлення"
    ]
    product_list.append(product_param)

for item in product_list:
    if len(item) > 2:
        print(f"Name: {item[0]} Old price: {item[1]} New price: {item[2]}")
    else:
        print(f"Name: {item[0]} Price: {item[1]}")
