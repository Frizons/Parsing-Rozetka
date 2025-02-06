import re
import requests
from bs4 import BeautifulSoup
import time


class Parser:

    def finding_item(self, url):

        soup_obj = self.get_soup_obj(url)

        find_content = self.get_content(soup_obj)

        try:
            find_pages_number = soup_obj.find_all("a", class_="pagination__link")
            count_pages = len(find_pages_number)
        except:
            count_pages = 1

        if count_pages == 1:
            self.get_item_info(find_content)
        else:
            self.get_item_info(find_content)

            for page_num in range(2, count_pages + 1):
                re_pattern = r"/c\d+/"
                re_pattern_end = r"/c\d+/\w+"
                finding_pattern = re.search(re_pattern, url)[0]

                try:
                    re.search(re_pattern_end, url)[0]
                    new_url = url.replace(
                        finding_pattern, f"{finding_pattern}page={page_num};"
                    )
                except:
                    new_url = url.replace(
                        finding_pattern, f"{finding_pattern}page={page_num}/"
                    )

                next_soup_obj = self.get_soup_obj(new_url)
                next_content = self.get_content(next_soup_obj)
                self.get_item_info(next_content)

    def get_soup_obj(self, url):
        get_page = requests.get(url)
        get_content = get_page.text
        soup_obj = BeautifulSoup(get_content, "html.parser")
        return soup_obj

    def get_content(self, soup_obj):
        return soup_obj.find_all("div", class_="goods-tile__content")

    def get_item_info(self, find_content):

        for item in find_content:
            find_name_item = item.find("span", class_="goods-tile__title")
            find_link_item = item.find("a")
            name_item = find_name_item.text
            link_item = find_link_item.get("href")

            try:
                find_old_price_item = item.select(
                    "div.goods-tile__price--old.price--gray"
                )
                if find_old_price_item:
                    find_new_price_item = item.select("span.goods-tile__price-value")
                    old_price = find_old_price_item[0].text
                    new_price = find_new_price_item[0].text

                    print(
                        f"Name: {name_item}; Price old: {old_price} Price new: {new_price}; Link: {link_item}"
                    )
                elif not find_old_price_item:
                    raise Exception("Item not found")
                else:
                    break
            except:
                find_price_item = item.select("span.goods-tile__price-value")
                if find_price_item:
                    regular_price = find_price_item[0].text

                    print(
                        f"Name: {name_item}; Price gerular: {regular_price}; Link: {link_item}"
                    )


notebooks = Parser()

notebooks.finding_item("https://rozetka.com.ua/ua/notebooks/c80004/")
