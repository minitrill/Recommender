# -*- coding: utf-8 -*-

import scrapy
import random
import json
import requests

from scrapy.http import Request, FormRequest
from user_video_spider.items import UserVideoSpiderItem
from user_video_spider.config import Config

from . import (
    LoadUserAgents
)

class UVSpider(scrapy.Spider):

    name = 'uvSpider'

    def __init__(self):
        self.allowed_domains = ['bilibili.com']
        self.uas = LoadUserAgents(Config.ROOTPATH + "user_video_spider/user_agents.txt")

    def start_requests(self):

        with open(Config.ROOTPATH+Config.FIDFILE, 'r') as f:
            line = f.readline()
            while (line):
                mid = int(line.split(' ')[0])
                fid = int(line.split(' ')[1])
                self.head = {
                    'Accept': '*/*',
                    'Accept-Encoding': 'gzip, deflate, br',
                    'Accept-Language': 'zh-CN,zh;q=0.9',
                    'Host': 'api.bilibili.com',
                    'Referer': 'https://space.bilibili.com/%d/' % (mid),
                    'User-Agent': ''
                }
                self.head['User-Agent'] = random.choice(self.uas)
                url = 'https://api.bilibili.com/x/v2/fav/video?vmid={}&ps=30&fid={}&tid=0&keyword=&pn=1&order=fav_time&jsonp=jsonps'.format(mid, fid)
                yield FormRequest(url=url, headers=self.head, method='GET', callback=self.parse, dont_filter=True)
                line = f.readline()

    def parse(self, response):

        item = UserVideoSpiderItem()
        content = json.loads(response.text)

        try:
            data = content['data']
            page_count = data['pagecount'] - 1
            item['mid'] = data['mid']
            item['fid'] = data['fid']
            item['tag'] = ''
            for t in data['tlist']:
                if(len(item['tag']) == 0):
                    item['tag'] += t['name']
                else:
                    item['tag'] += ('|' + t['name'])

            archives = data['archives']

            if(page_count > 0):
                for i in range(page_count):
                    url = 'https://api.bilibili.com/x/v2/fav/video?vmid={}&ps=30&fid={}&tid=0&keyword=&pn={}&order=fav_time&jsonp=jsonps'.format(item['mid'], item['fid'], i+2)
                    content1 = json.loads(requests.get(url=url,headers=self.head).text)
                    archives += content1['data']['archives']

            item['aid_list'] = []
            for archive in archives:
                user_video = {}
                user_video['aid'] = archive['aid']
                user_video['pubdate'] = archive['pubdate']
                user_video['ctime'] = archive['ctime']
                user_video['fav_time'] = archive['fav_at']
                user_video['videos'] = archive['videos']
                user_video['tag'] = archive['tname']
                user_video['stat'] = archive['stat']
                item['aid_list'].append(user_video)

            # print(item, '\n', len(item['aid_list']))
            yield item
        except Exception as e:
            print('Failed!!! The reason:\n', e)