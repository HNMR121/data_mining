
from pathlib import Path
import requests
import time
import json





headers = {
    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
url = 'https://5ka.ru/api/v2/categories/'

response = requests.get(url, headers = headers)

result_json_file = Path(__file__).parent.joinpath('cat.json')

# result_html_file = Path(__file__).parent.joinpath('5ka.html')

result_json_file.write_text(response.text, encoding='UTF-8')


a = 1
