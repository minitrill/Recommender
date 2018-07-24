# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class userItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    # status = scrapy.Field()
    mid = scrapy.Field()
    name = scrapy.Field()
    sex = scrapy.Field()
    rank = scrapy.Field()
    face = scrapy.Field()
    regtime = scrapy.Field()
    spacesta = scrapy.Field()
    birthday = scrapy.Field()
    sign = scrapy.Field()
    level = scrapy.Field()
    officialverify_type = scrapy.Field()
    officialverify_desc = scrapy.Field()
    viptype = scrapy.Field()
    vipstatus = scrapy.Field()
    toutu = scrapy.Field()
    toutuid = scrapy.Field()

    following = scrapy.Field()
    follower = scrapy.Field()

    archiveview = scrapy.Field()
    article = scrapy.Field()

    video_num = scrapy.Field()

    like_video_num = scrapy.Field()

    tag = scrapy.Field()

    subtag = scrapy.Field()

    coins = scrapy.Field()


class userFollowItem(scrapy.Item):

	mid = scrapy.Field()
