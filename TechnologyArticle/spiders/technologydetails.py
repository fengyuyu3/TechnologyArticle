# -*- coding: utf-8 -*-
import scrapy
from scrapy_redis.spiders import RedisSpider
from selenium import webdriver
from scrapy.xlib.pydispatch import dispatcher
from scrapy import signals
from TechnologyArticle.items import TechnologyDetailsItem
from w3lib.html import remove_tags
import time
import re

class TechnologydetailsSpider(RedisSpider):
    name = 'technologydetails'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.jianshu.com/p/8abb412a0000']
    redis_key = "technologydetails:start_urls"

    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="G:\python-3.6.3\Scripts\chromedriver.exe")
        # self.browser = webdriver.PhantomJS(executable_path="E:\python\Scripts\phantomjs.exe")
        super(TechnologydetailsSpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        #当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def parse(self, response):
        item = TechnologyDetailsItem()
        item["title"] = response.xpath('//h1[@class="title"]/text()').extract()[0]
        item["publish_time"] = response.xpath('//span[@class="publish-time"]/text()').extract()[0].split("*")[0]
        item["wordage"] = "0" if len(response.xpath('//span[@class="wordage"]/text()').extract()) <= 0 else re.sub("\D", "",response.xpath('//span[@class="wordage"]/text()').extract()[0])
        item["views_count"] = "0" if len(response.xpath('//span[@class="views-count"]/text()').extract()) <= 0 else re.sub("\D", "", response.xpath('//span[@class="views-count"]/text()').extract()[0])
        item["comments_count"] = "0" if len(response.xpath('//span[@class="comments-count"]/text()').extract()) <= 0 else re.sub("\D", "", response.xpath('//span[@class="comments-count"]/text()').extract()[0])
        item["likes_count"] = "0" if len(response.xpath('//span[@class="likes-count"]/text()').extract()) <= 0 else re.sub("\D", "", response.xpath('//span[@class="likes-count"]/text()').extract()[0])
        # item["content"] = remove_tags(response.xpath('//div[@class="show-content"]').extract()[0])
        item["content"] = response.text
        item["url"] = response.url
        print(item["content"])
        yield item

    def getNum(self,str):
        c = re.compile("/+d")
        s = re.match(str,c)
        return s
