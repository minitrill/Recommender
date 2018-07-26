# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

import os

from user_video_spider.config import Config

class UserVideoSpiderPipeline(object):

    def process_item(self, item, spider):
        count = self.read_count()
        if(count['fav_line'] >= Config.NUMOFLINE or count['favorite_number'] == 0):
            count['fav_line'] = 0
            count['favorite_number'] += 1
            with open(Config.ROOTPATH+Config.FAVPREFIX+str(count['favorite_number'])+Config.POSTFIX, 'w') as f:
                f.write(Config.FIRSTLINE_FAV)
                f.close()

        if(count['vid_line'] >= Config.NUMOFLINE or count['video_number'] == 0):
            count['vid_line'] = 0
            count['video_number'] += 1
            with open(Config.ROOTPATH+Config.VIDEOPREFIX+str(count['video_number'])+Config.POSTFIX, 'w') as f:
                f.write(Config.FIRSTLINE_VID)
                f.close()

        if(count['beh_line'] >= Config.NUMOFLINE or count['behavior_number'] == 0):
            count['beh_line'] = 0
            count['behavior_number'] += 1
            with open(Config.ROOTPATH+Config.BEHAVIORPREFIX+str(count['behavior_number'])+Config.POSTFIX, 'w') as f:
                f.write(Config.FIRSTLINE_BEH)
                f.close()


        with open(Config.ROOTPATH+Config.FAVPREFIX+str(count['favorite_number'])+Config.POSTFIX, 'a') as f:
            new_line = '"%d", "%d", "%s"\n' % (item['mid'], item['fid'], item['tag'])
            f.write(new_line)
            count['fav_line'] += 1
            f.close()

        new_line_vidoes = []
        new_line_behaviors = []

        for i in item['aid_list']:
            new_line_v = '"%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%d", "%s"\n' % \
                           (i['stat']['aid'],
                            i['stat']['coin'],
                            i['stat']['danmaku'],
                            i['stat']['favorite'],
                            i['stat']['his_rank'],
                            i['stat']['like'],
                            i['stat']['dislike'],
                            i['stat']['now_rank'],
                            i['stat']['reply'],
                            i['stat']['share'],
                            i['stat']['view'],
                            i['tag'])
            new_line_b = '"%d", "%d", "%d", "%d", "%d", "%d"\n' % (item['mid'], i['aid'], i['videos'], i['pubdate'], i['ctime'], i['fav_time'])
            new_line_vidoes.append(new_line_v)
            new_line_behaviors.append(new_line_b)

        with open(Config.ROOTPATH+Config.VIDEOPREFIX+str(count['video_number'])+Config.POSTFIX, 'a') as f:

            for i in new_line_vidoes:
                f.write(i)
                count['vid_line'] += 1
            f.close()

        with open(Config.ROOTPATH+Config.BEHAVIORPREFIX+str(count['behavior_number'])+Config.POSTFIX, 'a') as f:
            for i in new_line_behaviors:
                f.write(i)
                count['beh_line'] += 1
            f.close()

        self.save_count(count)


        return item

    def read_count(self):
        count = {}

        with open(Config.ROOTPATH+Config.COUNTFILE, 'r') as f:
            line = f.readline()
            for i in line.split(';'):
                for j in i.split(','):
                    k = j.split(':')
                    try:
                        count[k[0]] = int(k[-1])
                    except:
                        pass
            f.close()
        return count

    def save_count(self, count):
        s = ''

        for i in Config.COUNTTYPE:
            s += i[0] + ':' + str(count[i[0]]) + ',' + i[1] + ':' + str(count[i[1]]) + ';'

        with open(Config.ROOTPATH+Config.COUNTFILE, 'w') as f:
            f.write(s)
            f.close()