#!/usr/bin/env python
# -*- coding:utf-8 -*-

import os

from data_handler import DataHandler
from database_handler import DatabaseHandler


def add_interest(data, db, filename):
    sentence = 'select interest from user_interest where mid=%s;'
    para = (data['mid'])
    interests = db.query_all_data(sentence, para)

    interest = ''
    for i in interests:
        if(len(interest) == 0):
            interest += i[0]
        else:
            interest += ('|' + i[0])
    s = ''
    for key, value in data.items():
        if(len(s) == 0):
            s += ('"%s":"%s"' % (key, value))
        else:
            s += (', ' + '"%s":"%s"' % (key, value))
    s += (', "interest":"%s"' % (interest) + '\n')
    with open(filename, 'a') as f:
        f.write(s)
        f.close()


if __name__ == '__main__':

    # configuration
    path = '/home/cls/文档/data_process/data/video/'
    host = '127.0.0.1'
    user = 'root'
    passwd = '123'
    db = 'bilibili'
    table = 'tags'

    dbhandler = DatabaseHandler(host, user, passwd, db)

    # try:
    #     cursor = dbhandler.connect.cursor()
    #     sentence = 'select interest from user_interest where mid=%s;'
    #     cursor.execute(sentence, ('966022'))
    #     result = cursor.fetchall()
    #     print(result[0][0])
    #     dbhandler.connect.commit()
    #     cursor.close()
    # except Exception as e:
    #     print(error_massage, e)

    # db_sentence = '''create table if not exists user_interest(id bigint not null auto_increment, mid bigint, interest varchar(10));'''
    # alter_primary = '''alter table user_interest add unique (mid, interest);'''
    # dbhandler.create_table(db_sentence)
    # dbhandler.create_table(alter_primary)

    files = os.listdir(path)

    # for fn in files:
    #     filename = path + fn
    #     print(filename)
    #     fdh = DataHandler(filename, 1)
    #     filename_ = path + 'new_' + fn 
    #     while(fdh.handleEachLine(add_interest, dbhandler, filename_)):
    #         pass


    for fn in files:
        filename = path + fn
        print(filename)
        fdh = DataHandler(filename, 0, ', ', r"\w+")
        while(fdh.handleEachLine(dbhandler.insert_data, table)):
            pass

    dbhandler.closedb()
