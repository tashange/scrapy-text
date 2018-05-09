# -*- coding: utf-8 -*-
from Douyu.items import DouyuItem
import scrapy
import json
class DouyuSpider(scrapy.Spider):
	name = 'douyu'
	allowed_domains = ['douyucdn.cn']
    
	baseURL = "http://capi.douyucdn.cn/api/v1/getVerticalRoom?limit=20&offset="
	offset = 0
	start_urls = [baseURL + str(offset)]
	def parse(self, response):
    	#取返回的json数据中的['data'],json.loads?
    	# data = json.loads(response.body)
    	# print data
		data_list = json.loads(response.body)['data']
		if len(data_list) == 0:
			return
		for data in data_list:
			item = DouyuItem()
			item['nickname'] = data["nickname"]
			item['imagelink'] = data["vertical_src"]
			yield item
		self.offset += 20
		yield scrapy.Request(self.baseURL + str(self.offset),callback = self.parse)
     #小技巧：ls | wc -l 显示当前文件下的文件个数