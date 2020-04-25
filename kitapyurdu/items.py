# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://docs.scrapy.org/en/latest/topics/items.html

import scrapy


class KitapyurduItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
   	name = scrapy.Field()
   	author = scrapy.Field()
   	author_id = scrapy.Field()
   	isbn = scrapy.Field()
   	description = scrapy.Field()
   	book_id = scrapy.Field()
   	publisher = scrapy.Field()
   	total_pages = scrapy.Field()
   	publish_date = scrapy.Field()
   	author = scrapy.Field()


