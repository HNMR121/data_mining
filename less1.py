from pathlib import Path
import requests

# url = 'https://5ka.ru/special_offers/'


# with open(result_html_file, encoding='UTF-8') as file:
#     file.write(response.text)

# params = {'store': None,
#           'records_per_page': 12,
#           'page': 1,
#           'categories': None,
#           'ordering': None,
#           'price_promo__gte': None,
#           'price_promo__lte': None,
#           'search': None}
#
# headers = {
#     'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}
# url = 'https://5ka.ru/api/v2/special_offers/'

# response = requests.get(url, params =params, headers = headers)
#
# result_json_file = Path(__file__).parent.joinpath('5ka.json')
#
# # result_html_file = Path(__file__).parent.joinpath('5ka.html')
#
# result_json_file.write_text(response.text, encoding='UTF-8')


a = 1


class Parse5ka:
    headers = {
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/88.0.4324.150 Safari/537.36'}

    def __init__(self, start_url: str, save_path: Path):
        self.start_url = start_url
        self.save_path = save_path

    def _get_


if __name__ == '__main__':
    url = 'https://5ka.ru/api/v2/special_offers/'
    save_path = Path(__file__).parent.joinpath('products')
    if not save_path.exists():
        save_path.mkdir()

    parser = Parse5ka(url, save_path)
