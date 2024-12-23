import requests
from bs4 import BeautifulSoup


class Parser:

    def finding_item(self, url):
        get_page = requests.get(url)
        get_content = get_page.text
        soup_obj = BeautifulSoup(get_content, "html.parser")
        find_content = soup_obj.find_all("div", class_="goods-tile__content")

        for item in find_content:
            find_name_item = item.find(
                "span", class_="goods-tile__title ng-star-inserted"
            )
            find_link_item = item.find("a", class_="ng-star-inserted")
            name_item = find_name_item.text
            link_item = find_link_item.get("href")

            try:
                find_old_price_item = item.select(
                    "div.goods-tile__price--old.price--gray.ng-star-inserted"
                )
                find_new_price_item = item.select("span.goods-tile__price-value")
                old_price = find_old_price_item[0].text
                new_price = find_new_price_item[0].text

                print(
                    f"Name: {name_item}; Price old: {old_price} Price new: {new_price}; Link: {link_item}"
                )
            except:
                find_price_item = item.find("p", class_="ng-star-inserted")
                regular_price = find_price_item.text

                print(
                    f"Name: {name_item}; Price gerular: {regular_price}; Link: {link_item}"
                )


notebooks = Parser()

notebooks.finding_item("https://rozetka.com.ua/ua/notebooks/c80004/")
