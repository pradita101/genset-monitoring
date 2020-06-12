#!/usr/bin/python3
# -*- coding: utf-8 -*-

import sys, traceback
import pymongo
import bson
import configparser

config = configparser.ConfigParser()
config.read('config.ini')

class Mongo_Models():

    def __init__(self):
        self.client = pymongo.MongoClient(config['MONGODB']['server'],int(config['MONGODB']['port']))
        self.db = self.client.genset_monitoring

    def insert_raw(self, data_raw):
        encoded_data = bson.encode(data_raw)
        insert_data = bson.decode(encoded_data)
        self.db.raw_data.insert_one(insert_data)


if __name__ == "__main__":

    try:
        mm = Mongo_Models()
        data_test = {"A":"DFXX","B":"1576563163","C":["-6.288","106.817","0.490","35.330"],"D":"1576563131","E":"1576563053","F":"131085","G":"-127.00","H":"0","I":"1","J":["4.84","5.19","4.26"],"K":["0.00","0.00","0.00"],"L":["0.00","0.00","0.00"],"M":"0.00","N":"0.00","O":"0.00","P":"0.00","Q":"0.00","R":"SAJ-alpha","S":["1","23,99","8","1","0","0","0","3593"]}
        mm.insert_raw(data_test)
    except Exception as e:
        print(e)
        traceback.print_exc(file=sys.stdout)
        pass