# -*- coding: utf-8 -*-
import scrapy
from Spider.items import SpiderItem
from Spider.common_util.common_util.datetime_util import add_date


class X360SpiderSpider(scrapy.Spider):
    name = 'x360_spider'
    allowed_domains = ['zhushou.360.cn']
    start_urls = ['http://zhushou.360.cn/list/index/cid/102139/?page=%s' % x for x in range(50)]

    def parse(self, response):
        item = SpiderItem()
        dt = add_date(0).strftime('%Y-%m-%d')
        apps = response.xpath('//*[@id="iconList"]/li')
        for app in apps:
            app_name = app.xpath('./h3/a/text()').extract()[0]
            apk_name = app.xpath('./a[2]/@href').extract()[0].split('/')[-1].replace('.apk', '')
            item['row'] = ','.join([dt, app_name, apk_name, '金融理财', '', '360应用市场'])
            yield item
