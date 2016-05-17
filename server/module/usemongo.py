#!/usr/bin/env python
# -*- coding:utf-8 -*-
import sys
from pymongo import MongoClient
from datetime import datetime

#connection
connect = MongoClient('localhost', 27017)

# SELECT DB 
db = connect.sensors
collect = db.gps

print "Called usemongo.py"

#データ登録
def set_gps(lat,lng):
    collect.save({"date":datetime.now(),"location":{"lat":lat,"lng":lng}})
    return "OK set_gps"

# データ表示
def get_gps():
    logs = []
    for data in collect.find():
        logs.append(data)
    print "logs",logs
    return logs

# 最新の一件を取得
def get_log_recent():
    recent_log = list(collect.find().sort('_id',-1).limit(1))
    print "recent_log: ",recent_log
    return recent_log

# 最新の一件のlat,lngを返す
def get_gps_now():
    for data in collect.find().sort('_id',-1).limit(1):
        lat = data["location"]["lat"]
        lng = data["location"]["lng"]
    return lat,lng

# 全ての位置情報をリストで返す
def get_gps_all():
    gps_list = []
    for data in collect.find().sort('_id',-1):
        tmp_list = []
        lat = data["location"]["lat"]
        lng = data["location"]["lng"]
        tmp_list.append(lat)
        tmp_list.append(lng)
        gps_list.append(tmp_list)
    return gps_list


if __name__ == "__main__":
#   set_gps(123,456)
#    get_gps()
#    print get_recent_gps()
#    print get_gps_now()
    print get_gps_all()
