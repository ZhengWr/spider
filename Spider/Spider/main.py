# encoding=utf-8
# coding=utf-8
from scrapy import cmdline
import os
import sys
from Spider.common_util.common_util.datetime_util import add_date
import time
from os.path import abspath, dirname


def re_write_file(file_path):
    f = open(file_path, 'w')
    f.write(','.join(['date', 'app_name', 'apk_name', 'big_class', 'label', 'market']) + '\n')
    f.close()


dt = add_date(0).strftime('%Y-%m-%d')
file_path = dirname(abspath(__file__))
file_list = ['%s\\%s'.replace('\\', '/') % (file_path, file) for file in os.listdir(file_path)]

re_write_file('%s/files/wdj_spider_%s.csv' % (file_path, dt))
re_write_file('%s/files/xm_spider_%s.csv' % (file_path, dt))
re_write_file('%s/files/tx_spider_%s.csv' % (file_path, dt))
re_write_file('%s/files/bd_spider_%s.csv' % (file_path, dt))
re_write_file('%s/files/x360_spider_%s.csv' % (file_path, dt))
re_write_file('%s/files/mmy_spider_%s.csv' % (file_path, dt))

os.system("scrapy crawl wdj_spider")
time.sleep(2)
os.system("scrapy crawl xm_spider")
time.sleep(2)
os.system("scrapy crawl tx_spider")
time.sleep(2)
os.system("scrapy crawl bd_spider")
time.sleep(2)
os.system("scrapy crawl x360_spider")
time.sleep(2)
#os.system("scrapy crawl mmy_spider")
#time.sleep(2)
#合并爬去的文件
os.system("python %s/common_util/scripts/spider_file_scripts/merge_files.py" % file_path)
