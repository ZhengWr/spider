# -*- coding: utf-8 -*-
import scrapy
from Spider.items import SpiderItem
from Spider.common_util.common_util.datetime_util import add_date


class MmySpiderSpider(scrapy.Spider):
    name = 'mmy_spider'
    allowed_domains = ['www.mumayi.com']
    start_urls = ['http://www.mumayi.com/android/gouwulicia/list_123_1.html']

    def parse(self, response):
        pages = int(response.xpath('//*[@id="ajaxPageArea"]/a/@href').extract()[-1].split('/')[-1].split('_')[-1].split('.')[0])
        print(pages)
        for i in range(pages):
            yield scrapy.Request(url='http://www.mumayi.com/android/gouwulicia/list_123_%s.html' % str(i+1), callback=self.parse_link)

    def parse_link(self, response):
        apps = response.xpath('/html/body/div[5]/div[2]/div[1]/ul/li')
        for app in apps:
            url = app.xpath('./a[1]/@href').extract()[0]
            yield scrapy.Request(url=url, callback=self.parse_page)

    def parse_page(self, response):
        item = SpiderItem()
        dt = add_date(0).strftime('%Y-%m-%d')
        try:
            app_name = response.xpath('/html/body/div[5]/div[1]/div[1]/h1/text()').extract()[0].replace(',', '&').split()[0]
            apk_name = response.xpath('/html/body/div[5]/div[1]/div[6]/div[1]/ul/li[2]/text()').extract()[0].replace(',', '&')
            item['row'] = ','.join([dt, app_name, apk_name, '金融理财', '', '木蚂蚁论坛'])
            yield item
        except Exception as e:
            print(e)