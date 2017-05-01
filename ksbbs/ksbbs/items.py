# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy
from scrapy import Field, Item


class KsbbsItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    title=Field()
    link=Field()
    author=Field()
    create_time=Field()
    update_time=Field()
    area=Field()