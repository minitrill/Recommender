#!/usr/bin/env python
# -*- coding:utf-8 -*-

import re

class DataHandler(object):
    """docstring for UserDataHandler"""
    def __init__(self, filename, number_nomean, split_pattern=',', re_pattern=r"'\w+'"):
        self.f = open(filename, 'r')
        for i in range(number_nomean):
            self.f.readline()
    
        key_line = self.f.readline().strip('\n').split(split_pattern)
        pattern = re.compile(re_pattern)
        self.keys = []
        for k in key_line:
            key = re.findall(r'\w+', pattern.findall(k)[0])[0]
            self.keys.append(key)

        # print(self.keys, len(self.keys))


    def handleEachLine(self, callback=None, *args):
        line = self.f.readline()
        if(not line):
            return False
        data = {}
        iterator = 0
        line = line.strip('\n')[1:-1]
        # print(line.split('", "'), len(line.split('", "')))
        for i in line.split('", "'):
            
            try:
                if(len(i) > 0 and i[0] == '"' and i[-1] != '"'):
                    # print(i.split(', '), iterator)
                    for j in i.split(', '):
                        if (len(j) > 0 and j[0] == '"'):
                            data[self.keys[iterator]] = j[1:]
                        else:
                            data[self.keys[iterator]] = j
                        iterator += 1
                    continue
                else:
                    data[self.keys[iterator]] = i
            except Exception as e:
                print(line, '\n', i, type(i), '\n', e)
                print(i, len(line.split('", "')), iterator, len(self.keys))
            iterator += 1
        if(callback != None):
            print(*args)
            callback(data, *args)
        # print(data)
        # print(self.keys)
        # for i in self.keys:
        #     try:
        #         print(data[i])
        #     except Exception as e:
        #         print(i,e)
        # print(len(data.keys()), len(self.keys))
        return True


if __name__ == '__main__':
    filename = '/home/cls/文档/data_process/data/user/user6.txt'
    UDH = DataHandler(filename, 1)
    while(UDH.handleEachLine()):
        pass
    # UDH.handleEachLine()
    UDH.f.close()

    filename1 = '/home/cls/文档/data_process/data/favorite/user_fav_1.txt'
    BDH = DataHandler(filename1, 0, ', ', r"\w+")
    BDH.handleEachLine()
    BDH.f.close()