# 豌豆荚爬虫
import scrapy
from Spider.items import SpiderItem
import datetime


# 通过命令行创建的此类 cmd: scrapy genspider wdj_spider wandoujia.com
class WdjSpiderSpider(scrapy.Spider):
    name = 'wdj_spider'
    allowed_domains = ['wandoujia.com']
    start_urls = ['http://www.wandoujia.com/category/5023_631/1', 'http://www.wandoujia.com/category/5023_628/1',
                  'http://www.wandoujia.com/category/5023_627/1', 'http://www.wandoujia.com/category/5023_958/1',
                  'http://www.wandoujia.com/category/5023_629/1', 'http://www.wandoujia.com/category/5023_955/1',
                  'http://www.wandoujia.com/category/5023_981/1', 'http://www.wandoujia.com/category/5023_1003/1']

    def parse(self, response):
        pages = int(response.xpath('/html/body/div[2]/div[2]/div/div[1]/div/div/a[12]/@href')\
                    .extract()[0].split('/')[-1])
        url = response.url[:-2]
        print(url, pages)
        for i in range(pages):
            yield scrapy.Request(url + '/' + str(i+1), callback=self.parse_page)

    def parse_page(self, response):
        app_counts = len(response.xpath('//*[@id="j-tag-list"]/li'))
        dt = datetime.datetime.now().strftime('%Y-%m-%d')
        dic_label = {'5023_631': '支付', '5023_628': '炒股', '5023_627': '银行', '5023_958': '理财记账', '5023_629': '彩票',
                    '5023_955': '借贷', '5023_981': '投资', '5023_1003': '保险'}
        label_code = response.url.split('/')[4]
        label = dic_label[label_code]
        for i in range(app_counts):
            item = SpiderItem()
            app_name = response.xpath('//*[@id="j-tag-list"]/li[%s]/div[2]/h2/a/text()' % (i+1)).extract()
            apk_name = response.xpath('//*[@id="j-tag-list"]/li[%s]/div[2]/h2/a/@href' % (i+1)).extract()
            if len(app_name) > 0 and len(apk_name) > 0:
                app_name = app_name[0].replace(',', '&')
                apk_name = apk_name[0].split('/')[-1].replace(',', '&')
                item['row'] = ','.join([dt, app_name, apk_name, '金融理财', label, '豌豆荚'])
                yield item









