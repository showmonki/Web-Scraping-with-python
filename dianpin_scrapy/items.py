# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# http://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class hljitem(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	title = scrapy.Field()
	excerpt = scrapy.Field()


class citylist(scrapy.Item):
	# define the fields for your item here like:
	# name = scrapy.Field()
	region = scrapy.Field()  # 地区
	prov = scrapy.Field()    # 省份
	city = scrapy.Field()    # 城市
	url = scrapy.Field()     # url前缀
	citycode = scrapy.Field()  # citycode
