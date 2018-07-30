#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
import pymysql as pm

class DatabaseHandler(object):
    """docstring for DatabaseHandler"""
    def __init__(self, host, user, passwd, db):
        self.connect = pm.connect(host=host,user=user,passwd=passwd,db=db,charset='utf8')
        

    def database_operation(self, sentence, error_massage):
        try:
            cursor = self.connect.cursor()
            cursor.execute(sentence)
            self.connect.commit()
            cursor.close()
        except Exception as e:
            print(error_massage, e)
            # sys.exit(0)

    def query_all_data(self, sentence, para):
        try:
            cursor = self.connect.cursor()
            cursor.execute(sentence, para)
            data = cursor.fetchall()
            self.connect.commit()
            cursor.close()
            return data
        except Exception as e:
            print(error_massage, e)

    def create_table(self, sentence):
        
        error_massage = "Can not create table!! Because: \n"
        self.database_operation(sentence, error_massage)


    def insert_data(self, data, table):
        
        error_massage = "Can not insert!! Because: \n"

        # for i in data['tag'].split('|'):
        #     sentence = '''insert into %s (interest) values ('%s')''' % (table, i)
        #     self.database_operation(sentence, error_massage)

        sentence = '''insert into %s (tag) values ('%s')''' % (table, data['tag'])
        self.database_operation(sentence, error_massage)

    def closedb(self):
        self.connect.close()