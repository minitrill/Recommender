# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
import pymysql as py

class UserSiderPipeline(object):
    def process_item(self, item, spider):
        try:
            conn = py.connect(host='127.0.0.1',user='root',passwd='123',db='bilibili',charset='utf8')
            cursor = conn.cursor()
            
            insert = '''
                    insert into users(archiveview,article,birthday,coins,
                    follower,following,level,mid,name,officialverify_desc,officialverify_type,rank,
                    regtime,sex,sign,spacesta,toutu,toutuid,vipstatus,viptype,video_num,like_video_num,face) values
                    ('%d','%d','%s','%d','%d','%d','%d','%d','%s','%s','%d','%d',
                    '%d','%s','%s','%d','%s','%d','%d','%d','%d','%d', '%s');
                ''' % (item['archiveview'],item['article'],item['birthday'],item['coins'],
                 item['follower'],item['following'],item['level'],
                item['mid'],item['name'],item['officialverify_desc'],item['officialverify_type'],
                 item['rank'],item['regtime'],item['sex'],item['sign'],item['spacesta'],
                item['toutu'],item['toutuid'],item['vipstatus'],item['viptype'],item['video_num'],item['like_video_num'],item['face'])
            cursor.execute(insert)
            conn.commit()
            cursor.close()
            conn.close()
        except Exception as e:
            print(e,item['mid'])

        return item

