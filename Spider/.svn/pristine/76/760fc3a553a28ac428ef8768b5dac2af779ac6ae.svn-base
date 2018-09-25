# -*- coding: utf-8 -*-
import scrapy
from Spider.items import SpiderItem
import json
import math
import datetime


class XmSpiderSpider(scrapy.Spider):
    name = 'xm_spider'
    allowed_domains = ['app.mi.com']
    start_urls = ['http://app.mi.com/categotyAllListApi']

    def parse(self, response):
        page_size = 30
        pages = int(json.loads(response.xpath('/html/body/p/text()').extract()[0])['count'])
        page_nums = math.ceil(pages/page_size)
        for i in range(page_nums):
            yield scrapy.Request('http://app.mi.com/categotyAllListApi?page=%s&categoryId=1&pageSize=30' % str(i), callback=self.parse_page)

    def parse_page(self, response):
        data = json.loads(response.xpath('/html/body/p/text()').extract()[0])['data']
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        for tem in data:
            item = SpiderItem()
            app_name = tem['displayName'].replace(',', '&')
            apk_name = tem['packageName'].replace(',', '&')
            item['row'] = ','.join([dt, app_name, apk_name, '金融理财', '', '小米应用市场'])
            yield item

