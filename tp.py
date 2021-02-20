
import json
# import pandas as pd
# dict = [{"parent_group_code":"585","parent_group_name":"Новый год"},
# {"parent_group_code":"938","parent_group_name":"Лучшее по акции"},
# {"parent_group_code":"939","parent_group_name":"Лидеры рейтинга"},
# {"parent_group_code":"940","parent_group_name":"14 февраля"},
# {"parent_group_code":"941","parent_group_name":"23 февраля"},
# {"parent_group_code":"942","parent_group_name":"Бодрый завтрак"}]

# print(dict[0])

params = {'store': None,
          'records_per_page': 12,
          'page': 1,
          'categories': None,
          'ordering': None,
          'price_promo__gte': None,
          'price_promo__lte': None,
          'search': None}
a = 12

params.update({'categories': a})
print(params)

from pathlib import Path
import requests
import time
import json
import re



#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
# url = 'https://5ka.ru/api/v2/categories/'

# response = requests.get(url, headers = headers)
# print(type(response))

# json_data = json.loads(response.text.split('['))
# print(response.text.replace("[","[",''))

# json_data = response.text.replace("[", '').replace("]", '')

# json_data = json.loads(json_data)
#
# print(type(json_data))

# my_str = "one dog, one cat, one rabbit"

# c = my_str.replace("one", "two", 2)
# print(c)


# list_cat = re.findall(r'\d+', response.text)



# with open('cat.json', encoding='UTF-8') as file:
#     for elem in file:
#         a = json.loads(elem)
#         print(a)
        # for key in elem:
            # print(key.items())
        # print(elem)
#     # a = json.loads(file)
#     # for i in a:
#     #     print(a)
# with open('cat.json', encoding='UTF-8') as file:
#     for i in file:
#         print(i)

# print(dict[0])



from pathlib import Path
import requests
import time
import json
import re

params = {'store': None,
          'records_per_page': 12,
          'page': 1,
          'categories': 940,
          'ordering': None,
          'price_promo__gte': None,
          'price_promo__lte': None,
          'search': None}

product_dict = {
"name": "имя категории",
"code": "Код соответсвующий категории (используется в запросах)",
"products": [{'товар1'},  {'товар2'}]
}


headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
url_cat = 'https://5ka.ru/api/v2/categories/'

response_cat = requests.get(url_cat, headers = headers)

# list_cat = re.findall(r'\d+', response_cat.text)

# a = int(list_cat[1])

# params.update({'categories': a})
# print(params)
# print(list_cat)

url = 'https://5ka.ru/api/v2/special_offers/'

response = requests.get(url, params =params, headers = headers)



print(type(response.text))

data = json.loads(response.text)

# print(data)
temp_dict = {}

# a = (data["results"]["name"])

print()
for i in data["results"]:
    # default_data.update({'item3': 3})
    # product_dict.update(i["name"])
    print(i)
    # print(i)

print(temp_dict)
# print(a)
# print(type(a))

a = 1
# result_json_file.write_text(response.text, encoding='UTF-8')

# result_json_file = Path(__file__).parent.joinpath('product.json')

# result_html_file = Path(__file__).parent.joinpath('5ka.html')

# result_json_file.write_text(response.text, encoding='UTF-8')
# print(data["results"][0]["name"])
