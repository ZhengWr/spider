import scrapy
from Spider.items import SpiderItem
import json
import datetime


class TxSpliderSpider(scrapy.Spider):
    name = 'tx_spider'
    allowed_domains = ['sj.qq.com']
    start_urls = ['http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=114&pageSize=20&pageContext=0']

    def parse(self, response):
        page_content = int(response.url.split('&')[-1].split('=')[1])
        result = json.loads(response.xpath('/html/body/p/text()').extract()[0])
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        if len(result['obj']) != 0:
            for tem in result['obj']:
                item = SpiderItem()
                app_name = tem['appName'].replace(',', '&')
                apk_name = tem['pkgName'].replace(',', '&')
                item['row'] = ','.join([dt, app_name, apk_name, '金融理财', '', '腾讯应用宝'])
                yield item
            page_content += 20
            yield scrapy.Request('http://sj.qq.com/myapp/cate/appList.htm?orgame=1&categoryId=114&pageSize=20&pageContext=%s' % page_content, callback=self.parse)
