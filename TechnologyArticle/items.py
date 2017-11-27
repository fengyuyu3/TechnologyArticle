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
    url = scrapy.Field()
    def get_insert_sql(self):
        #插入知乎question表的sql语句
        print(type(self["title"]))
        print(type(self["wordage"]))
        print(type(self["views_count"]))
        print(type(self["comments_count"]))
        print(type(self["likes_count"]))
        print(type(self["content"]))
        print(type(self["url"]))

        create_time = datetime.datetime.strptime(self["publish_time"],SQL_DATETIME_FORMAT)
        print(type(create_time))

        # insert_sql = """
        #     insert into technology_info(title, publish_time, wordage, views_count, comments_count, likes_count, content,url
        #       ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)ON DUPLICATE KEY UPDATE wordage=VALUES(wordage),views_count=VALUES(views_count)
        #       ,likes_count=VALUES(likes_count),comments_count=VALUES(comments_count)
        # """
        insert_sql = """
            insert into technology_info(title, publish_time, wordage, views_count, comments_count, likes_count, content,url
              ) VALUES (%s, %s, %s, %s, %s, %s, %s,%s)ON DUPLICATE KEY UPDATE wordage=VALUES(wordage),views_count=VALUES(views_count)
              ,likes_count=VALUES(likes_count),comments_count=VALUES(comments_count)
        """
        params = (
            self["title"], create_time, self["wordage"],
            self["views_count"], self["comments_count"], self["likes_count"],
            self["content"], self["url"]
        )

        return insert_sql, params

