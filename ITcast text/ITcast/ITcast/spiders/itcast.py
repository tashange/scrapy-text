# -*- coding: utf-8 -*-
#json�ļ����ص����ַ���unicode����,����sysģ����Խ��������Ҫ�ڹܵ��ļ�������ſ��ԣ���Ϊ���Ĭ�ϵ�����������uncode
# import sys
# reload(sys)
# sys.setdefaultencoding("utf-8")

import scrapy
from ITcast.items import ItcastItem

class ITcastSpider(scrapy.Spider):
#name��start_urlsΪ���������allowed_domainsΪ��ѡ����(��ʱΪ�˲������淶Χ���ƣ���д)
    name = "itcast"
    allowed_domains = ["itcast.cn"]
	#��ʼURL�б�����Ϊ���url��ַ���ԣ��ָ�
    start_urls = ["http://www.itcast.cn/channel/teacher.shtml"]

    def parse(self, response):
		node_list = response.xpath("//div[@class='li_txt']") #�ڵ�
		# items = [] #item�б������洢���е�item�ֶεģ������õ��˹ܵ��ļ����Բ�����,����д��for���治Ȼֻ���õ����ص�����һ���ֶ���
		for node in node_list:
		#����item�ֶζ��������洢��Ϣ��ǰ��������һ���࣬����Ҫ�õ�ÿ�����ص��ֶΣ����Ծ���for���洴��
			item = ItcastItem()
			#node.xpath���ص���xpath����.extract()��xpath����ת��Ϊ��unicode�ַ���(���ã���ȡ�ֶβ�ת��Ϊ�ַ���)
			name = node.xpath("./h3/text()").extract() #����item['name'] = node.xpath("./h3/text()").extract()[0]������ֿ�д��
			title = node.xpath("./h4/text()").extract()
			info = node.xpath("./p/text()").extract()

			#xpath���ص��ǰ���һ��Ԫ�ص��б�
			# print name[0]
			# print title[0]
			# print info[0]
			item['name'] = name[0]
			item['title'] = title[0]
			item['info'] = info[0]
			# items.append(item) #�����ص�item�ֶηŵ��б���
			#������ȡ����ÿ��item���ݣ����ܵ��ļ������´�ִ��ʱ�᷵�ص��˴�����ִ�к���Ĵ��룬return��ֱ��ִ����͹ر��˺���
			yield item
		# ֱ�ӷ����������
		# return items