# -*- coding: utf-8 -*-

import os

PREFIX = 'user'
POSTFIX = '.txt'
FILENUM = 10
FILEPATH = '/home/ubuntu/userSpider/data/'
FIRSTLINE = 'number:0\n'
SECONDLINE = "item['mid'],item['name'],item['birthday'],item['rank'],item['regtime'],item['sex'],item['video_num'],item['like_video_num'],item['follower'],item['following'],item['archiveview'],item['article'],item['coins'],item['level'],item['spacesta'],item['sign'],item['tag'],item['subtag'],item['vipstatus'],item['viptype'],item['toutu'],item['toutuid'],item['officialverify_desc'],item['officialverify_type'],item['face']\n"

def makefile():
	for i in range(FILENUM):
		filename = FILEPATH + PREFIX + str(i+1) + POSTFIX
		if(os.path.isfile(filename) == False):
			with open(filename, 'w') as f:
				f.write(FIRSTLINE)
				f.write(SECONDLINE)
				f.close()



if __name__ == '__main__':
	makefile()
