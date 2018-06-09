# -*- coding: utf-8 -*-
# import scrapy


# class Jb51SpiderSpider(scrapy.Spider):
    # name = 'jb51_spider'
    # allowed_domains = ['jb51.net']
    # start_urls = ['http://jb51.net/']

    # def parse(self, response):
        # pass
# -*- coding:utf-8 -*-
import scrapy
from scrapy.http import Request
import web
import time
import pymysql


db = web.database(dbn='mysql', host='127.0.0.1', db='imchenkun', user='root', pw='root')

# �����վ����
allow_domain = "jb51.net"

base_url = "http://www.jb51.net"

# �б�ҳ
list_url = "http://www.jb51.net/list/list_%d_%d.htm"

# �б��ҳ
list_page = 1

# ����ҳ
crawl_url = "http://www.jb51.net/article/%d.htm"


class JB51Spider(scrapy.Spider):
    name = "jb51"
    start_urls = [
        "http://www.jb51.net/list/index_1.htm"
    ]

    cate_list = []

    def parse(self, response):
        cate_id = response.selector.xpath('//div[@class="index_bor clearfix"]/div[@class="index_con"]/span/a/@href').re('(\d+)')[::2]
        for id in cate_id:
            cate_url = list_url % (int(id), 1)
            yield Request(cate_url, callback=self.parse_page)

    def parse_page(self, response):
        _params = response.selector.xpath('//div[@class="dxypage clearfix"]/a[last()]/@href').re('(\d+)')
        cate_id = int(_params[0]) # ������
        count = int(_params[1]) # ��ҳ��

        article_urls = response.selector.xpath('//div[@class="artlist clearfix"]/dl/dt/a/@href').extract()
        # �����һҳ
        for article_url in article_urls:
            yield Request(base_url + article_url, callback=self.parse_article)

        # ��������ҳ
        for page in range(1, count):
            url = (list_url % (cate_id, page + 1))
            yield Request(url, callback=self.parse_list)

    def parse_list(self, response):
        """���������б�"""
        article_urls = response.selector.xpath('//div[@class="artlist clearfix"]/dl/dt/a/@href').extract()
        for article_url in article_urls:
            yield Request(base_url + article_url, callback=self.parse_article)

    def parse_article(self, response):
        """������������"""
        title = response.selector.xpath('//div[@class="title"]/h1/text()').extract()[0]
        content = response.selector.xpath('//div[@id="content"]').extract()[0]
        tags = ','.join(response.selector.xpath('//div[@class="tags mt10"]/a/text()').extract())
        
        results = db.query('select count(0) as total from articles where origin=$origin', vars = { 'origin': response.url })
        if results[0].total <= 0:
            db.insert('articles',
                      title=title,
                      origin=response.url,
                      content=content,
                      add_date=int(time.time()),
                      hits=0,
                      tags=tags
            )
