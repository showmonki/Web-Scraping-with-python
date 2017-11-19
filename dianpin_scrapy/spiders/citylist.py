# -*- coding: utf-8 -*-
import re
import scrapy
from scrapy.http import Request
from dianpin_scrapy.items import citylist

class dianpincity(scrapy.Spider):
	name = "citylist"
	allowed_domains = ["dianping.com"]
	start_urls =['http://www.dianping.com/citylistguonei']

	def parse(self, response):
		nodes = response.xpath('//*[ @ id = "divArea"]/li/dl[@class="terms"]/dd/a')
		for node in nodes:
			item = citylist()
			address = node.xpath('.//@href')[0].extract()
			url = ('http://www.dianping.com' + address)
			item['city'] = node.xpath('.//strong/text()').extract()
			item['prov'] = node.xpath('./../../dt/text()').extract()
			item['region'] = node.xpath('./../../../strong/text()').extract()
			item['url'] = url
			yield Request(url, meta={'key': item},
									 callback=self.parse_code)


	def parse_code(self, response):
			item = response.meta['key']
			# citycode = response.url
			shopall = response.xpath('//*[@class="i-search"]/span/input').extract()
			citycode = re.findall('data-s-cityid=\"([0-9]+)\"', str(shopall))
			item['citycode'] = citycode
			yield item
