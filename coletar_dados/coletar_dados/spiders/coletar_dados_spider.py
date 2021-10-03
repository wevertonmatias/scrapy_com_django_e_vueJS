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

    def parse(self, response):
        data = response.css(".quote")

        for line in data:
            item = ColetarDadosItem()
            item['citacao'] = line.css(".text::text").extract_first()
            item['autor'] = line.css(".author::text").extract_first()
            yield item