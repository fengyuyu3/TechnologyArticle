# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy_redis.spiders import RedisSpider
from TechnologyArticle.items import TechnologyarticleItem
from scrapy.xlib.pydispatch import dispatcher
from selenium import webdriver
from scrapy import signals
import redis
import time

class TechnologySpider(RedisSpider):
    name = 'technology'
    redis_key = "technology:start_urls"
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    # r.lpush(redis_key, "http://www.jianshu.com/c/3fde3b545a35")
    def __init__(self):
        self.browser = webdriver.Chrome(executable_path="G:\python-3.6.3\Scripts\chromedriver.exe")
        # self.browser = webdriver.PhantomJS(executable_path="E:\python\Scripts\phantomjs.exe")
        super(TechnologySpider, self).__init__()
        dispatcher.connect(self.spider_closed, signals.spider_closed)

    def spider_closed(self, spider):
        # 当爬虫退出的时候关闭chrome
        print("spider closed")
        self.browser.quit()

    def parse(self, response):
        item = TechnologyarticleItem()
        urls = response.xpath('//div[@class="content"]/a/@href')
        for url in urls:
            url = parse.urljoin(response.url, url.extract())
            self.r.lpush("technologydetails:start_urls", url)
            item["url"] = url
            yield item
        # pass
