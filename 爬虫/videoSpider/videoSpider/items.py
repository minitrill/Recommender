# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class VideospiderItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    aid = scrapy.Field()
    coin = scrapy.Field()
    danmaku = scrapy.Field()
    favorite = scrapy.Field()
    his_rank = scrapy.Field()
    like = scrapy.Field()
    no_reprint = scrapy.Field()
    now_rank = scrapy.Field()
    reply = scrapy.Field()
    share = scrapy.Field()
    view = scrapy.Field()

    tag = scrapy.Field()
