# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os
import sys

PREFIX = 'video_info_'
POSTFIX = '.txt'
FILENUM = 100
FILEPATH = '/home/cls/文档/crawl/LouisSpider/videoSpider/data/'
MAXIMUN = 10000

class VideospiderPipeline(object):

    def __init__(self):
        self.filename, self.lines, self.fnum = self.check_full()


    def check_full(self):
        for i in range(FILENUM):
            filename = PREFIX + str(i+1) + POSTFIX
            with open(FILEPATH + filename, 'r') as f:
                lines = f.readlines()
                num = int(lines[0].split(':')[-1])
                f.close()
                if(num < MAXIMUN):
                    return filename, lines, num
        return None, None

    def process_item(self, item, spider):
        try:
            print("item: ")
            if(self.lines == None or self.fnum == None):
                sys.exit(0)

            with open(FILEPATH + self.filename, 'w') as f:
                new_line = '"%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%s"\n' % \
                           (item['aid'],
                            item['coin'],
                            item['danmaku'],
                            item['favorite'],
                            item['his_rank'],
                            item['like'],
                            item['no_reprint'],
                            item['now_rank'],
                            item['reply'],
                            item['share'],
                            item['view'],
                            item['tag'])
                self.lines.append(new_line)
                self.fnum += 1
                self.lines[0] = 'number:' + str(self.fnum) + '\n'
                for line in self.lines:
                    f.write(line)
                f.close()

            if(self.fnum > MAXIMUN):
                    self.filename, self.lines, self.fnum = self.check_full()

        except Exception as e:
            print(e,item['mid'])
