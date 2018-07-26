# -*- coding: utf-8 -*-


class Config(object):

    ROOTPATH = '/home/cls/文档/crawl/LouisSpider/user_video_spider/'

    COUNTFILE = 'data/count.txt'
    FIDFILE = 'data/fid_list.txt'

    COUNTTYPE = [['favorite_number', 'fav_line'], ['video_number', 'vid_line'], ['behavior_number', 'beh_line']]

    FAVPREFIX = 'data/favorite/user_fav_'
    VIDEOPREFIX = 'data/video/video_info_'
    BEHAVIORPREFIX = 'data/behavior/behavior_info_'
    POSTFIX = '.txt'

    FIRSTLINE_FAV = "mid, fid, tag\n"
    FIRSTLINE_VID = 'aid, coin, danmaku, dislike, favorite, his_rank, like, now_rank, reply, share, view, tag\n'
    FIRSTLINE_BEH = 'mid, aid, videos, fav_time, ctime, pubdate\n'

    NUMOFLINE = 10000
