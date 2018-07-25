# -*- coding: utf-8 -*-

import os

PREFIX = 'video_info_'
POSTFIX = '.txt'
FILENUM = 100
FILEPATH = '/home/cls/文档/crawl/LouisSpider/videoSpider/data/'
FIRSTLINE = 'number:0\n'
SECONDLINE = "(item['aid'],item['coin'],item['danmaku'],item['favorite'],item['his_rank'],item['like'],item['no_reprint'],item['now_rank'],item['reply'],item['share'],item['view'], item['tag'])\n"
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