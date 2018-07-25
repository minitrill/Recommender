# -*- coding: utf-8 -*-

import json
import time
import scrapy
import random
import requests
import numpy as np
from scrapy.http import Request, FormRequest

from videoSpider.items import VideospiderItem
from . import (
    LoadUserAgents,
    VIDEONUM
)


class VideoInfoSpider(scrapy.Spider):

    name = 'videoSpider'

    def __init__(self):
        self.allowed_domains = ['bilibili.com']

    def start_requests(self):

        uas = LoadUserAgents("/home/cls/文档/crawl/LouisSpider/userSpider/UserSider/user_agents.txt")

        for aid in set(np.random.randint(300000, 20000000,size=VIDEONUM)):
        # aid = 9426860
            self.head = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'api.bilibili.com',
                'Origin': 'https://www.bilibili.com',
                'Referer': 'https://www.bilibili.com/video/av{}/?spm_id_from=333.334.home_popularize.3'.format(aid),
                'User-Agent': ''
            }
            self.head['User-Agent'] = random.choice(uas)
            print(self.head['User-Agent'])
            url = 'https://api.bilibili.com/x/web-interface/archive/stat?aid={}'.format(aid)
            yield FormRequest(url=url, headers=self.head, method='GET', callback=self.parse, dont_filter=True)

    def parse(self, response):

        item = VideospiderItem()
        content = json.loads(response.text)

        try:

            data = content['data']
            ts = int(time.time() * 1000)
            url1 = 'https://api.bilibili.com/x/tag/archive/tags?callback=jqueryCallback_bili_5&aid={}&jsonp=jsonp&_={}'.format(data['aid'], ts)
            content1 = json.loads(requests.get(url=url1,headers=self.head).text[22:-1])

            item['aid'] = data['aid']
            item['coin'] = data['coin']
            item['danmaku'] = data['danmaku']
            item['favorite'] = data['favorite']
            item['his_rank'] = data['his_rank']
            item['like'] = data['like']
            item['no_reprint'] = data['no_reprint']
            item['now_rank'] = data['now_rank']
            item['reply'] = data['reply']
            item['share'] = data['share']
            item['view'] = data['view']

            item['tag'] = ''
            for i in content1['data']:
                if(len(item['tag']) == 0):
                    item['tag'] += i['tag_name']
                else:
                    item['tag'] += ('|' + i['tag_name'])

            yield item

        except Exception as e:
            print('Failed!!! The reason:\n', e)
            