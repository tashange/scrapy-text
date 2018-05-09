# -*- coding: utf-8 -*-

# Define your item pipelines here
#
# Don't forget to add your pipeline to the ITEM_PIPELINES setting
# See: https://doc.scrapy.org/en/latest/topics/item-pipeline.html

#重命名组件
import os
import scrapy
# #读取配置文件
# 下面这两个引用的位置不一样但效果是一样的
from settings import IMAGES_STORE as images_store
#from scrapy.utils.project import get_project_settings

#这里对图片处理要使用图片管道的方法
from scrapy.pipelines.images import ImagesPipeline
#from scrapy.utils.project import get_project_settings
class DouyuPipeline(ImagesPipeline):

 	def get_media_requests(self,item,info):
 		image_link = item['imagelink']
 		yield scrapy.Request(image_link)
 	def item_completed(self,results,item,info):
 		image_path = [x["path"] for ok,x in results if ok]
 		os.rename(images_store + image_path[0],images_store + item["nickname"] + ".jpg")
 		return item
  		