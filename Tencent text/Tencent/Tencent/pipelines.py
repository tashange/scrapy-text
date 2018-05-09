# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
# 第三步
import json
class TencentPipeline(object):
	def __init__(self):
		self.f = open("tencent.json","w")

	def process_item(self, item, spider):
		content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
		self.f.write(content)
		return item

	def close_spider(self,spider):
		self.f.close()