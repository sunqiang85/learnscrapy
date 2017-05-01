# -*- coding: utf-8 -*-
import scrapy
from ksbbs.items import KsbbsItem
from scrapy.selector import Selector
from scrapy.http import Request

class ArticleSpider(scrapy.Spider):
    name = "article"
    #allowed_domains = ["www.ksbbs.com"]
    #start_urls = ['http://www.ksbbs.com/thread-htm-fid-1309.html','http://www.ksbbs.com/thread-htm-fid-113.html'] #环保
    start_urls = ['http://www.ksbbs.com/thread-htm-fid-1309.html'] #环保
    url = 'http://www.ksbbs.com/'


    def parse(self,response):
        #print response.body
        item=KsbbsItem()
        selector=Selector(response)
        articles=selector.xpath('//tr[@class="tr3"]')
        area=selector.xpath('//h2[@class="mr5 fl f14"]/text()').extract()
        #print "----------------------articles-------------------"
        #print len(articles)
        for a in articles:
            #title=a.xpath('td[@class="subject"]/a[@class="subject_t f12"]/text()|td[@class="subject"]/a[@class="subject_t f12"]/b/font/text()').extract()
            title=a.xpath('td[@class="subject"]/a[@class="subject_t f12"]/text()|td[@class="subject"]/a[@class="subject_t f12"]/*/text()|td[@class="subject"]/a[@class="subject_t f12"]/*/*/text()').extract()

            rlink=a.xpath('td[@class="subject"]/a/@href').extract()
            author=a.xpath('td[@class="author"][1]/a/text()').extract()
            create_time=a.xpath('td[@class="author"][1]/p/text()').extract()
            update_time=a.xpath('td[@class="author"][2]/p/text()').extract()
            #if len(title)==0:
            #    continue
            item['title']=title
            item['author']=author
            item['link']=rlink
            item['create_time']=create_time
            item['update_time']=update_time
            item['area']=area

            #print "============================================"
            #print rlink
            #item['link']=rlink
            yield item
            nextLink = selector.xpath('//a[@class="pages_next"]/@href').extract()
            # 第10页是最后一页，没有下一页的链接
        if nextLink:
            nextLink = nextLink[0]

            yield Request(self.url + nextLink, callback=self.parse)