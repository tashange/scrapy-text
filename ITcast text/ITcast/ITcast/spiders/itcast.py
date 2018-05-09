# -*- coding: utf-8 -*-
#json文件返回的是字符串unicode编码,引入sys模块可以解决，不过要在管道文件中输出才可以，因为框架默认的输出编码就是uncode
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import scrapy
from ITcast.items import ItcastItem

class ITcastSpider(scrapy.Spider):
#name和start_urls为必需参数，allowed_domains为可选参数(有时为了不受爬虫范围限制，不写)
    name = "itcast"
    allowed_domains = ["itcast.cn"]
	#起始URL列表，可以为多个url地址，以，分隔
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
		node_list = response.xpath("//div[@class='li_txt']") #节点
		# items = [] #item列表，用来存储所有的item字段的，后面用到了管道文件所以不用了,不能写到for里面不然只能拿到返回的最后的一个字段名
		for node in node_list:
		#创建item字段对象，用来存储信息，前面引入了一个类，我们要拿到每个返回的字段，所以就在for下面创建
			item = ItcastItem()
			#node.xpath返回的是xpath对象，.extract()将xpath对象转换为的unicode字符串(作用：提取字段并转换为字符串)
			name = node.xpath("./h3/text()").extract() #等于item['name'] = node.xpath("./h3/text()").extract()[0]，这里分开写了
			title = node.xpath("./h4/text()").extract()
			info = node.xpath("./p/text()").extract()

			#xpath返回的是包含一个元素的列表
			# print name[0]
			# print title[0]
			# print info[0]
			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] = info[0]
			# items.append(item) #将返回的item字段放到列表中
			#返回提取到的每个item数据，给管道文件处理，下次执行时会返回到此处继续执行后面的代码，return是直接执行完就关闭了函数
			yield item
		# 直接返回最后数据
		# return items