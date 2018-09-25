# -*- coding: utf-8 -*-
import scrapy
from Spider.items import SpiderItem
from Spider.common_util.common_util.datetime_util import add_date


class BdSpiderSpider(scrapy.Spider):
    name = 'bd_spider'
    allowed_domains = ['shouji.baidu.com']
    start_urls = ['http://shouji.baidu.com/software/510/']

    def parse(self, response):
        pages = int(response.xpath('//*[@id="doc"]/div[3]/div[2]/ul/li')[-2].xpath('./a/@href').extract()[0].split('.')[0].split('_')[1])
        for i in range(pages):
            yield scrapy.Request(url='http://shouji.baidu.com/software/510/list_%s.html' % str(i+1), callback=self.parse_page)

    def parse_page(self, response):
        item = SpiderItem()
        dt = add_date(0).strftime('%Y-%m-%d')
        apps = response.xpath('//*[@id="doc"]/div[3]/div[1]/div/ul/li')
        for app in apps:
            app_name = app.xpath('./a/div/p[3]/span/@data_name').extract()[0].replace(',', '&')
            apk_name = app.xpath('./a/div/p[3]/span/@data_package').extract()[0].replace(',', '&')
            item['row'] = ','.join([dt, app_name, apk_name, '金融理财', '', '百度应用市场'])
            yield item