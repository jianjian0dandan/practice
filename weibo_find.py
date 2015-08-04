# -*- coding: utf-8 -*-
import os
import re
import time
import datetime
import csv
import sys
reload(sys)
sys.setdefaultencoding('utf-8')

MONGOD_HOST = '219.224.135.47'
MONGOD_PORT = 27019

def default_mongo(host=MONGOD_HOST, port=MONGOD_PORT, usedb='54api_weibo_v2'):
    connection = pymongo.MongoClient(host=host, port=port, j=True, w=1)
    db = connection.admin
    db = getattr(connection, usedb)
    return db

def read1():
    idlist = []
    path = '/home/gina/python/practice/source/all_uidlist.txt'
    uid_file = open(path,'r')
    for line in uid_file:
        idlist.append(line)
    return idlist

def read2():
    userlist = []
    user_file = csv.reader(file('/home/gina/python/practice/weibo_user.csv','rb'))
    for line in user_file:
        userlist.append(line)
    return userlist

def out():
    uidlist = read1()
    msglist = read2()
    items = []
    path = '/home/gina/python/practice/weibo_find_out.csv'
    csvfile = open(path,'wb')   
    writer = csv.writer(csvfile) 

    for uid in uidlist:
        i = 0
        for msg in msglist:
            print msg
            if msg == uid :
                i = 1 + i
            break
        if i == 0:
             writer.writerow([uid])
       
    csvfile.close() 

if __name__ == '__main__':
   out()