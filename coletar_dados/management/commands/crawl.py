from django.core.management.base import BaseCommand
from scrapy.crawler import CrawlerProcess
from scrapy.settings import Settings

from coletar_dados.coletar_dados import settings as minha_conf
from coletar_dados.coletar_dados.spiders.coletar_dados_spider import ColetarDadosSpider

class Command(BaseCommand):
    help = "Coletar dados"

    def handle(self, *args, **options):
        crawler_settings = Settings()
        crawler_settings.setmodule(minha_conf)

        process = CrawlerProcess(settings=crawler_settings)

        process.crawl(ColetarDadosSpider)
        process.start()