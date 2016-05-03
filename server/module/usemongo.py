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

print "Called ctr_mongo.py"

#データ登録
def set_gps(lat,lng):
    collect.save({"date":datetime.now(),"location":{"lat":lat,"lng":lng}})
    return "OK set_gps"

if __name__ == "__main__":
   set_gps(123,456)
