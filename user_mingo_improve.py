# -*- coding: utf-8 -*-
import os
import re
import time
import redis
import socket
import pymongo
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

def read():
    idlist = []
    path = '/home/jiangln/all_uidlist.txt'
    uid_file = open(path,'r')
    for line in uid_file:
        idlist.append(line)
    return idlist

def out():
    uidlist = read()
    #items = []
    db = default_mongo()
    path = '/home/jiangln/weibo_user_no.csv'
    csvfile = open(path,'wb')
    writer = csv.writer(csvfile)
    for uid in uidlist:
        try:
            query = {"_id":int(uid)}
            if db.master_timeline_user.find(query).count()>0:
                pass
            else:
                writer.writerow([uid])
        except ValueError:
            writer.writerow([uid])
    csvfile.close()

if __name__ == '__main__':
    out()
