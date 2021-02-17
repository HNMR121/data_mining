
import json
# import pandas as pd
dict = [{"parent_group_code":"585","parent_group_name":"Новый год"},
{"parent_group_code":"938","parent_group_name":"Лучшее по акции"},
{"parent_group_code":"939","parent_group_name":"Лидеры рейтинга"},
{"parent_group_code":"940","parent_group_name":"14 февраля"},
{"parent_group_code":"941","parent_group_name":"23 февраля"},
{"parent_group_code":"942","parent_group_name":"Бодрый завтрак"}]

# print(dict[0])


from pathlib import Path
import requests
import time
import json
import re




headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
url = 'https://5ka.ru/api/v2/categories/'

response = requests.get(url, headers = headers)

print(type(response.text))

list_cat = re.findall(r'\d+', response.text)



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



