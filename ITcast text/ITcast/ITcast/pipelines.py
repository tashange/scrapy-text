# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html
#�ܵ��ļ������Ǵ���item������
#ItcastPipeline�ö����Ӧsettings.py�ļ��еĹܵ���Ҫ����
import json
class ItcastPipeline(object):
#��ʼ�������ļ�
	def __init__(self):
		self.f = open("itcast_pipeline.json","w")
#����itcast.py�ļ���ÿ��item���ݲ�ת��dirt�ֵ��ʽ������תΪencode��ʽ��������
	def process_item(self, item, spider):
		content = json.dumps(dict(item),ensure_ascii = False) + ",\n"
		self.f.write(content.encode("utf-8"))
		return item
		#���������ر�
	def close_spider(self,spider):
		self.f.close()