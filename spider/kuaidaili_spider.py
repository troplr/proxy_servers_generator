#coding:utf-8
"""
@file:      kuaidaili_spider.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    Vim
@create:    2017-2-16 14:18
@description:

"""
import os,sys
sys.path.append(os.path.dirname(sys.path[0]))

from page_parser.kuaidaili import Parser,KuaiProxyServer
from multiprocessing.dummy import Pool as ThreadPool
#from request_with_proxy import request_with_random_ua

import requests
import time

class KuaiSpider:
    """
        http://www.kuaidaili.com/free/outtr/
    """
    def __init__(self,url):
        parser = Parser(
            html_source = self.own_req(url).text
        )
        self.first_page_url = url
        self.page_num = parser.get_page_num()
        print(self.page_num)
        time.sleep(2)

    def own_req(self,url):
        return requests.get(url,
            headers={
                'cookie': 'channelid=0; sid=1487245785393826; _ga=GA1.2.312655308.1487237144; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487237142; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487246847',
                'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
            }
        )

    def crawl_per_page(self,page_index):
        print('---------- page {}  ------------'.format(page_index))
        page_url = '{}/{}'\
            .format(self.first_page_url,page_index)
        print(page_url)
        for i in range(10):
            try:
                parser = Parser(
                    html_source=self.own_req(page_url).text
                )
                break
            except:
                print('req error')

        for sec in parser.get_sections():
            server = KuaiProxyServer(sec)
            server.show_in_cmd()
            if server.save_to_db():
                print('save ok')
            else:
                print('save error')

    def run(self,thread_cot=1):
        pool = ThreadPool(thread_cot)
        page_range = range(1,self.page_num)
        print(page_range)
        pool.map(self.crawl_per_page,page_range)


if __name__=="__main__":
    KuaiSpider(url='http://www.kuaidaili.com/free/outha').run()