# -*- coding: utf-8 -*-

# Define here the models for your scraped items
#
# See documentation in:
# https://doc.scrapy.org/en/latest/topics/items.html

import scrapy


class ItcastItem(scrapy.Item):
    # define the fields for your item here like:
	#��ʦ����
	name = scrapy.Field()
	#��ʦְ��
	title = scrapy.Field()
	#��ʦ��Ϣ
	info = scrapy.Field()
    #pass