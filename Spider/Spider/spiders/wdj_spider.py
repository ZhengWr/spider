# 豌豆荚爬虫
import scrapy
from urllib.parse import urlparse
import json
from lxml import etree
from Spider.items import SpiderItem
import datetime



# 通过命令行创建的此类 cmd: scrapy genspider wdj_spider wandoujia.com
class WdjSpiderSpider(scrapy.Spider):
    name = 'wdj_spider'
    allowed_domains = ['wandoujia.com']
    start_urls = ['https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=631&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=628&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=627&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=629&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=981&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=958&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=955&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr',
                  'https://www.wandoujia.com/wdjweb/api/category/more?catId=5023&subCatId=1003&page=1&ctoken=3-_B84SSP0m6j1EH6ZabKwJr']



    def parse(self, response):

        dic_label = {'5023_631': '支付', '5023_628': '炒股', '5023_627': '银行', '5023_958': '理财记账', '5023_629': '彩票',
                     '5023_955': '借贷', '5023_981': '投资', '5023_1003': '保险'}
        parse_url = urlparse(response.url).query
        querys = parse_url.split('&')
        label_code1 = querys[0].split('=')[1]
        label_code2 = querys[1].split('=')[1]
        label_code = label_code1 + "_" + label_code2
        label = dic_label[label_code]

        setting = json.loads(response.body)
        crrrpage = setting['data']['currPage']
        content = setting['data']['content']
        result = etree.HTML(content)

        if crrrpage!=-1:
            dt = datetime.datetime.now().strftime('%Y-%m-%d')
            apps = result.xpath('//li')
            for app in apps:
                item = SpiderItem()
                app_name = app.xpath('./a[2]/@data-app-name')[0]
                apk_name=app.xpath('./a[2]/@data-app-pname')[0]

                item['row'] = ','.join([dt, app_name, apk_name, '金融理财', label, '豌豆荚'])
                yield  item
            yield scrapy.Request('https://www.wandoujia.com/wdjweb/api/category/more?catId=' +label_code1 +'&subCatId=' +label_code2 +'&page=' + str(crrrpage+1) + '&ctoken=3-_B84SSP0m6j1EH6ZabKwJr', callback=self.parse)










