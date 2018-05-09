# -*- coding: utf-8 -*-
# 第二步
import scrapy
from Tencent.items import TencentItem

class TencentSpider(scrapy.Spider):
    name = 'tencent'
    allowed_domains = ['tencent.com']
    #start_urls = ['http://tencent.com/']
    #需要拼接的URL
    baseURL = "http://hr.tencent.com/position.php?&start="
    #需要拼接的URL偏移量，实现翻页取值
    offset = 0 
    #爬虫启动时，读取的URL地址列表
    start_urls = [baseURL + str(offset)]
    def parse(self, response):
        #|或(不同的标签要用|，同一个标签下用or或者是and表示) &与 //tr[@class='even'] | //tr[@class='odd']存放信息的结果集
        #提取每个response的数据
    	node_list = response.xpath("//tr[@class='even'] | //tr[@class='odd']")

    	for node in node_list:
            #构建item对象，用来保存数据
    		item = TencentItem()
            #提取每个职位信息并转换编码，xpath是从1开始取数据的
    		item['positionName'] = node.xpath("./td[1]/a/text()").extract()[0].encode("utf-8")
    		
    		item['positionLink'] = node.xpath("./td[1]/a/@href").extract()[0].encode("utf-8")
    		
    		#若职位类别有为空的，则会报错，可以做一个判断，确认是否有返回值
    		if len(node.xpath("./td[2]/text()")):
    			item['positionType'] = node.xpath("./td[2]/text()").extract()[0].encode("utf-8")
    			
    		else:
    			item['positionType'] = "Null"
    		
    		item['peopleNumber'] = node.xpath("./td[3]/text()").extract()[0].encode("utf-8")
    		
    		item['workLocation'] = node.xpath("./td[4]/text()").extract()[0].encode("utf-8")
    		
    		item['publishTime'] = node.xpath("./td[5]/text()").extract()[0].encode("utf-8")
    		yield item
        #第一种方法：定数爬取(自创词)：只能爬到2190页。适用场景：页面没有可以点击的请求链接，必须通过拼接URL才能获取响应
		# if self.offset < 2190:
		# 	self.offset += 10
		# 	url = self.baseURL + str(self.offset)
		# 	yield scrapy.Request(url,callback = self.parse)
        # pass
        # 第二种方法：定'下一页'爬取(自创词)：根据点击下一页来进行爬取，不论数据增或减，都可以爬取到。
        # 直接从response获取需要爬取的链接，并发送请求处理，知道链接全部提取完成
        # 问题点:什么时候结束，这里会用到xpath的->
        # <-组合查询://a[@class="noactive" and @id="next"] 下一页  //a[@id="next"]/@href 取出来的值->
        # <-是一个链接需要拼接https://hr.tencent.com/才有效
        # xpath中不允许存在多个双引号，正则可以
        if len(response.xpath("//a[@class='noactive' and @id='next'] ")) == 0:#找到结束点‘下一页’
            url = response.xpath("//a[@id='next']/@href").extract()[0]
            yield scrapy.Request("https://hr.tencent.com/" + url,callback = self.parse)