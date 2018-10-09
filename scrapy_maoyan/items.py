# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

from scrapy import Field, Item

class NewsItem(Item):
    collection = 'maoyan'
    rank = Field()
    movie_name = Field()
    actor = Field()
    time = Field()
    score = Field()



