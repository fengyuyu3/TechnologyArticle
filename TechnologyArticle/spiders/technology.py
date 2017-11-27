# -*- coding: utf-8 -*-
import scrapy
from urllib import parse
from scrapy_redis.spiders import RedisSpider
import redis

class TechnologySpider(RedisSpider):
    #RedisSpider
    name = 'technology'
    # allowed_domains = ['www.baidu.com']
    # start_urls = ['http://www.jianshu.com/c/3fde3b545a35']
    # http://www.jianshu.com/c/3fde3b545a35
    redis_key = "technology:start_urls"
    pool = redis.ConnectionPool(host='127.0.0.1', port=6379)
    r = redis.Redis(connection_pool=pool)
    r.lpush(redis_key, "http://www.jianshu.com/c/3fde3b545a35")
    def parse(self, response):
        urls = response.xpath('//div[@class="content"]/a/@href')
        for url in urls:
            url = parse.urljoin(response.url, url.extract())
            # self.r.lpush(self.redis_key, url)
            self.r.lpush("test:start_urls", url)
        # pass
