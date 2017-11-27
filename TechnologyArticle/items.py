# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html
import datetime
import scrapy
from scrapy.loader import ItemLoader
from scrapy.loader.processors import MapCompose, TakeFirst, Join
from TechnologyArticle.settings import SQL_DATETIME_FORMAT


class TechnologyarticleItem(scrapy.Item):
    # define the fields for your item here like:
    # name = scrapy.Field()
    url = scrapy.Field()

    def get_insert_sql(self):
        #插入知乎question表的sql语句
        insert_sql = """
            insert into url_list(url) VALUES (%s)
              ON DUPLICATE KEY UPDATE url=VALUES(url)
        """
        params = (
            self["url"]
        )
        print("item   "+self["url"])
        return insert_sql, params

class TechnologyarticleItemLoader(ItemLoader):
    # default_item_class = TechnologyarticleItem
    # default_input_processor = MapCompose(lambda s: s.strip())
    default_output_processor = TakeFirst()
    # description_out = Join()

class TechnologyDetailsItemLoader(ItemLoader):
    # default_item_class =
    default_output_processor = TakeFirst()

class TechnologyDetailsItem(scrapy.Item):
    title = scrapy.Field()
    publish_time = scrapy.Field()
    wordage = scrapy.Field()
    views_count = scrapy.Field()
    comments_count = scrapy.Field()
    likes_count = scrapy.Field()
    content = scrapy.Field()
    def get_insert_sql(self):
        #插入知乎question表的sql语句
        insert_sql = """
            insert into zhihu_answer(title, publish_time, wordage, views_count, comments_count, likes_count, content
              ) VALUES (%s, %s, %s, %s, %s, %s, %s)
        """
        create_time = datetime.datetime.fromtimestamp(self["publish_time"]).strftime(SQL_DATETIME_FORMAT)
        params = (
            self["title"], create_time, self["wordage"],
            self["views_count"], self["comments_count"], self["likes_count"],
            self["content"]
        )
        return insert_sql, params

