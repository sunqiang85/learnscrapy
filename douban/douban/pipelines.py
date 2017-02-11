# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: http://doc.scrapy.org/en/latest/topics/item-pipeline.html
from items import DoubanItem
from scrapy.conf import settings
import pymongo

class DoubanPipeline(object):
    def __init__(self):
        host=settings['MONGODB_HOST']
        port=settings['MONGODB_PORT']
        dbName=settings['MONGODB_DBNAME']
        docName=settings['MONGODB_DOCNAME']

        client = pymongo.MongoClient(host,port)
        tdb = client[dbName]
        self.post = tdb[docName]
    def process_item(self, item, spider):
        movieInfo=dict(item)
        print '=============pipline============='
        self.post.insert(movieInfo)
        return item
