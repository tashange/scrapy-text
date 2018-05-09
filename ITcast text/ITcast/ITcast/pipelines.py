# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#管道文件，就是处理item的数据
#ItcastPipeline该对象对应settings.py文件中的管道，要开启
import json
class ItcastPipeline(object):
#初始化保存文件
	def __init__(self):
		self.f = open("itcast_pipeline.json","w")
#接收itcast.py文件的每个item数据并转换dirt字典格式，中文转为encode格式，并返回
	def process_item(self, item, spider):
		content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
		self.f.write(content.encode("utf-8"))
		return item
		#爬虫结束后关闭
	def close_spider(self,spider):
		self.f.close()