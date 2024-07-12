import re
import requests
import json

url = requests.get(
    "https://rozetka.com.ua/ua/notebooks/c80004/sort=rank/",
)

convert_page = url.text
patter = r"(?<=with_groups=1\":{\"body\":{\"data\":).*?(?=},\"headers\":{\"server\")"
find_str = convert_page
finding_name = re.search(patter, find_str)[0]
new_str = finding_name
str_to_list = json.loads(new_str)

with open("test_page.txt", "w", encoding="utf-8") as file_safe:
    file_safe.write(new_str)

for item in str_to_list:
    print("Name:", item["title"], "Price:", item["price"])
