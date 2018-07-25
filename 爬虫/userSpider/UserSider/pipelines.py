# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as py
import os
import sys

PREFIX = 'user'
POSTFIX = '.txt'
FILENUM = 10
FILEPATH = '/home/ubuntu/userSpider/data/'
MAXIMUN = 10000

class UserSiderPipeline(object):

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
        return None, None, None

    def process_item(self, item, spider):
        try:
            if(self.lines == None or self.fnum == None):
                sys.exit(0)

            with open(FILEPATH + self.filename, 'w') as f:
                new_line = '"%d", "%s", "%s", "%d", "%d", "%s", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%s", "%s", "%s", "%d", "%d", "%s", "%d", "%s", %d, "%s"\n' % \
                                         (item['mid'],item['name'],item['birthday'],item['rank'],item['regtime'],item['sex'],
                                         item['video_num'],item['like_video_num'],item['follower'],item['following'],
                                         item['archiveview'],item['article'],item['coins'],item['level'],item['spacesta'],
                                         item['sign'],item['tag'],item['subtag'],item['vipstatus'],item['viptype'],
                                         item['toutu'],item['toutuid'],item['officialverify_desc'],item['officialverify_type'],item['face'])
                self.lines.append(new_line)
                self.fnum += 1
                self.lines[0] = 'number:' + str(self.fnum) + '\n'
                for line in self.lines:
                    f.write(line)
                f.close()

            with open(FILEPATH + 'fid_list.txt', 'a') as f1:
                for fid in item['fid_list']:
                    s = '{} {}\n'.format(item['mid'], fid)
                    f1.write(s)
                f1.close()

            # conn = py.connect(host='127.0.0.1',user='root',passwd='123',db='bilibili',charset='utf8')
            # cursor = conn.cursor()
            
            # insert = '''
            #         insert into users(archiveview,article,birthday,coins,
            #         follower,following,level,mid,name,officialverify_desc,officialverify_type,rank,
            #         regtime,sex,sign,spacesta,toutu,toutuid,vipstatus,viptype,video_num,like_video_num,face,tag,subtag) values
            #         ('%d','%d','%s','%d','%d','%d','%d','%d','%s','%s','%d','%d',
            #         '%d','%s','%s','%d','%s','%d','%d','%d','%d','%d', '%s', '%s', '%s');
            #     ''' % (item['archiveview'],item['article'],item['birthday'],item['coins'],
            #      item['follower'],item['following'],item['level'],
            #     item['mid'],item['name'],item['officialverify_desc'],item['officialverify_type'],
            #      item['rank'],item['regtime'],item['sex'],item['sign'],item['spacesta'],
            #     item['toutu'],item['toutuid'],item['vipstatus'],item['viptype'],item['video_num'],item['like_video_num'],item['face'],item['tag'],item['subtag'])
            # cursor.execute(insert)
            # conn.commit()
            # cursor.close()
            # conn.close()
            if(self.fnum >= MAXIMUN):
                self.lines = None
                self.filename, self.lines, self.fnum = self.check_full()

        except Exception as e:
            print(e,item['mid'])

        return item

