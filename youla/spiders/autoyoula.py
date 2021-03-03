import scrapy


class AutoyoulaSpider(scrapy.Spider):
    name = 'autoyoula'
    allowed_domains = ['auto.youla.ru']
    start_urls = ['https://auto.youla.ru/']

    _css_selectors ={
        'brands' : '.TransportMainFilters_brandsList__2tIkv \
        .ColumnItemList_container__5gTrc a.blackLink',

    }

    def parse(self, response, *args, **kwargs):
        brands = response.css(self._css_selectors['brands'])
        for brands_a in brands:
            link = brands_a.attrib.get("href")
            yield response.follow(link, callback=self.brand_parse)
        print(1)

    def brand_parse(self,response):
        pass
