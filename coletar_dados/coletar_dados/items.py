# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html
from scrapy_djangoitem import DjangoItem
from core.models import Citacoes

# import scrapy


class ColetarDadosItem(DjangoItem):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # pass
    django_model= Citacoes
