import re
import random
import numpy as np
import json
import scrapy
import time
import requests
from bs4 import BeautifulSoup
from scrapy.http import Request, FormRequest
from UserSider.items import userItem

class Myspider(scrapy.Spider):
    """docstring for Myspider"""

    name = 'UserSider'
    allowed_domains = ['bilibili.com']
    bash_url = 'https://space.bilibili.com/ajax/member/GetInfo'
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'space.bilibili.com',
        'Origin': 'https://space.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' % random.randint(10000, 50000),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def start_requests(self):
        

        # for userId in range(32000, 42000):
        def LoadUserAgents(uafile):
            uas = []
            with open(uafile, 'rb') as uaf:
                for ua in uaf.readlines():
                    if ua:
                        uas.append(ua.strip()[1:-1 - 1])
            random.shuffle(uas)
            return uas


        uas = LoadUserAgents("/home/cls/文档/crawl/LouisSpider/userSpider/UserSider/user_agents.txt")
        for i in set(np.random.randint(100000, 399999,size=10000)):
            body = {
                'mid': str(i),
                'csrf': 'null',
            }
            self.head['User-Agent'] = random.choice(uas)
            yield FormRequest(url=self.bash_url, headers=self.head,method='POST',callback=self.parse,formdata=body, dont_filter=True)

    def parse(self, response):

        item = userItem()
        content = json.loads(response.text)
        data = content['data']
        # print('There are data of user: \n', data, '\n')

        try:
            # item['status'] = content['status'] if 'status' in data.keys() else 'False'
            item['mid'] = data['mid']
            item['name'] = data['name']
            item['sex'] = data['sex']
            item['rank'] = data['rank']
            item['face'] = data['face']
            item['regtime'] = data['regtime']
            item['spacesta'] = data['spacesta']
            item['birthday'] = data['birthday'] if 'birthday' in data.keys() else 'miss'
            item['sign'] = data['sign']
            item['level'] = data['level_info']['current_level']
            item['officialverify_type'] = data['official_verify']['type']
            item['officialverify_desc'] = data['official_verify']['desc']
            item['viptype'] = data['vip']['vipType']
            item['vipstatus'] = data['vip']['vipStatus']
            item['toutu'] = data['toutu']
            item['toutuid'] = data['toutuId']
            item['coins'] = data['coins']
            # print('successful1 get userinfo:' + str(data['mid']), '\n' + item['regtime'])
        except Exception as e:
            print('error1:',item['mid'],e)

        try:
            Header = {
                'Accept': '*/*',
                'Accept-Encoding': 'gzip, deflate, br',
                'Accept-Language': 'zh-CN,zh;q=0.9',
                'Host': 'api.bilibili.com',
                'Referer': 'https://space.bilibili.com/%d/' % int(data['mid']),
                'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
            }
            Header['User-Agent'] = self.head['User-Agent']
            url1 = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp&callback=__jp3'.format(int(data['mid']))
            content1 = json.loads(requests.get(url=url1,headers=Header).text[6:-1])
            # print('Content1: \n',content1, '\n')
            item['following'] = content1['data']['following']
            item['follower'] = content1['data']['follower']

            url2 = 'https://api.bilibili.com/x/space/upstat?mid={}&jsonp=jsonp&callback=__jp4'.format(int(data['mid']))
            content2 = json.loads(requests.get(url=url2,headers=Header).text[6:-1])
            # print('Content1: \n',content2, '\n')
            item['archiveview'] = content2['data']['archive']['view']
            item['article'] = content2['data']['article']['view']

            url3 = 'https://api.bilibili.com/x/space/navnum?mid={}&jsonp=jsonp&callback=__jp2'.format(int(data['mid']))
            content3 = json.loads(requests.get(url=url3,headers=Header).text[6:-1])
            # print('Content1: \n',content3, '\n')
            item['video_num'] = int(content3['data']['album']) + int(content3['data']['article']) + int(content3['data']['audio']) + int(content3['data']['video'])

            url4 = 'https://api.bilibili.com/x/space/fav/nav?mid={}&jsonp=jsonp&callback=__jp12'.format(int(data['mid']))
            content4 = json.loads(requests.get(url=url4,headers=Header).text[7:-1])
            item['like_video_num'] = 0
            for i in content4['data']['archive']:
                item['like_video_num'] += int(i['cur_count'])

            url5 = 'https://space.bilibili.com/ajax/member/getTags?mids={}'.format(int(data['mid']))
            content5 = json.loads(requests.get(url=url5,headers=self.head).text)
            item['tag'] = ''
            for i in content5['data']:
                for s in i['tags']:
                    if(len(item['tag']) == 0):
                        item['tag'] += s
                    else:
                        item['tag'] += ('|' + s)

            url6 = 'https://space.bilibili.com/ajax/tags/getSubList?mid={}'.format(int(data['mid']))
            content6 = json.loads(requests.get(url=url6,headers=self.head).text)
            item['subtag'] = ''
            for i in content6['data']['tags']:
                if(len(item['subtag']) == 0):
                    item['subtag'] += i['name']
                else:
                    item['subtag'] += ('|' + i['name'])

            # print('Content1: \n',content4, '\n')
        except Exception as e:
            print('Failed!!! The reason:\n', e)

        print(item)
        yield item
        
