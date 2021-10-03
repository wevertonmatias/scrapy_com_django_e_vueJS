# from scrapy.spiders import CrawlSpider, Rule
# from scrapy.linkextractors import LinkExtractor
# from scrapy.loader import ItemLoader
# from scrapy.loader.processors import TakeFirst

# from scraper.scraper.items import ScraperItem

import scrapy
from coletar_dados.coletar_dados.items import ColetarDadosItem

class ColetarDadosSpider(scrapy.Spider):
    name = "coletar_dados_spider"
    start_urls = ["https://quotes.toscrape.com/"]

    def parse(self, response, **kwargs):
        data = response.css(".quote")

        for line in data:
            item = ColetarDadosItem()
            item['citacao'] = line.css(".text::text").extract_first()
            item['autor'] = line.css(".author::text").extract_first()
            yield item
    
        proxima_pagina = response.css(".pager .next a::attr(href)").extract_first()

        if proxima_pagina:
            proxima_url = "https://quotes.toscrape.com/{}".format(proxima_pagina)
            yield scrapy.Request(url=proxima_url, callback=self.parse)
