from pathlib import Path

import requests
import bs4
from urllib.parse import urljoin
import pymongo



class MagnitParse:
    def __init__(self, start_url, db_client):
        self.start_url = start_url
        self.db = db_client['data_mining']
        self.collection = self.db['magnit_products']



    def _get_response(self, url):
        # TODO: написать обработку ошибки
        return requests.get(url)

    def _get_soup(self, url):
        response = self._get_response(url)
        return bs4.BeautifulSoup(response.text, 'lxml')

    def run(self):
        soup = self._get_soup(self.start_url)
        catalog = soup.find('div',attrs = {"сatalogue__main"})
        for prod_a in catalog.find_all('a', recursive=False):
            product_data = self._parse(prod_a)
            self._save(self._parse(prod_a))


    def get_template(self):
        return{
            'title': lambda a: a.find('div', attrs={'class': "card-sale__title"}).text,
            'url': lambda a: urljoin(self.start_url, a.attrs.get('href', '')),
            'promo_name': lambda a: a.find('div', attrs={'class': "card-sale__name"}).text
        }


    def _parse(self, product_a):
        data = {}
        for key,funk in self.get_template().items():
            try:
                data[key] = funk(product_a)
            except AttributeError:
                pass

        return data



    def _save(self, data: dict):
        self.collection.insert_one(data)
        print(1)

def get_save_path(dir_name):
    dir_path = Path(__file__).parent.joinpath(dir_name)
    if not dir_path.exists():
        dir_path.mkdir()
    return dir_path

if __name__ == '__main__':
    url = "https://magnit.ru/promo/"
    save_path = get_save_path('magnit_product')
    db_client = pymongo.MongoClient('mongodb://localhost:27017')
    parser = MagnitParse(url, db_client)
    parser.run()
