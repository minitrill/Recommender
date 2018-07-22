import re
import random
import json
import scrapy
import requests
from bs4 import BeautifulSoup
from scrapy.http import Request, FormRequest
from practice1.items import userItem

class Myspider(scrapy.Spider):
    """docstring for Myspider"""

    name = 'practice1'
    allowed_domains = ['bilibili.com']
    bash_url = 'https://space.bilibili.com/ajax/member/GetInfo'
    head = {
        'Accept': 'application/json, text/plain, */*',
        'Accept-Encoding': 'gzip, deflate, br',
        'Accept-Language': 'zh-CN,zh;q=0.9',
        'Host': 'space.bilibili.com',
        'Origin': 'https://space.bilibili.com',
        'Referer': 'https://space.bilibili.com/%d/' % random.randint(1,1000),
        'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; Win64; x64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/67.0.3396.99 Safari/537.36'
    }

    def start_requests(self):
        

        # for userId in range(32000, 42000):


        body = {
            'mid': '282994',
            'csrf': 'null',
        }
        yield FormRequest(url=self.bash_url, headers=self.head,method='POST',callback=self.parse,formdata=body)

    def parse(self, response):

        item = userItem()
        content = json.loads(response.text)
        data = content['data']
        print('There are data of user: \n', data, '\n')

        try:
            item['status'] = content['status'] if 'status' in data.keys() else 'False'
            item['mid'] = data['mid']
            item['name'] = data['name']
            item['sex'] = data['sex']
            item['rank'] = data['rank']
            item['face'] = data['face']
            try:
                item['regtime'] = time.strftime("%Y-%m-%d %H:%M:%S",time.localtime(data['regtime']))
            except:
                item['regtime'] = 'miss'
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
            print('successful1 get userinfo:' + str(data['mid']))
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
            url1 = 'https://api.bilibili.com/x/relation/stat?vmid={}&jsonp=jsonp&callback=__jp3'.format(int(data['mid']))
            content1 = json.loads(requests.get(url=url1,headers=Header).text[6:-1])
            print('Content1: \n',content1, '\n')

            url2 = 'https://api.bilibili.com/x/space/upstat?mid={}&jsonp=jsonp&callback=__jp4'.format(int(data['mid']))
            content2 = json.loads(requests.get(url=url2,headers=Header).text[6:-1])
            print('Content1: \n',content2, '\n')

            url3 = 'https://api.bilibili.com/x/space/navnum?mid={}&jsonp=jsonp&callback=__jp2'.format(int(data['mid']))
            content3 = json.loads(requests.get(url=url3,headers=Header).text[6:-1])
            print('Content1: \n',content3, '\n')

            url4 = 'https://api.bilibili.com/x/space/fav/nav?mid={}&jsonp=jsonp&callback=__jp12'.format(int(data['mid']))
            content4 = json.loads(requests.get(url=url4,headers=Header).text[7:-1])

            print('Content1: \n',content4, '\n')
        except Exception as e:
            print('Failed!!! The reason:\n', e)

        
