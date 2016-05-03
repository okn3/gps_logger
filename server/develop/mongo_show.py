#!/usr/bin/env python
# -*- coding:utf-8 -*-

import sys
from pymongo import MongoClient
from datetime import datetime

#connection
connect = MongoClient('localhost', 27017)

#testdbを取得
db = connect.sensors
#次のような記述もOK db = con['test']

#db名を出力
print "db name is = "
print db.name

#collectionの指定
collect = db.gps
#次のような記述もOK col = db['foo']


#最初に格納されているドキュメントを検索
#print "find_one = "
#print collect.find_one()

#コレクションに登録されているドキュメント全部を検索
print "find = "
for data in collect.find():
#        del data["_id"] #json dump用
        print data

#条件を指定してドキュメントを検索
print "find_query = "
for data in collect.find({'lat':130}):
    print data
