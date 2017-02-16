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

from page_parser.kuaidaili import Parser,KuaiProxyServer
from multiprocessing.dummy import Pool as ThreadPool
import requests

class KuaiSpider:
    """
        http://www.kuaidaili.com/free/outtr/
    """
    def __init__(self,url):
        parser = Parser(
            html_source = self.own_rq(url).text
        )
        self.first_page_url = url
        self.page_num = parser.get_page_num()
        print(self.page_num)

    def own_rq(self,url):
        for i in range(10):
            try:
                return requests.get(url,
                    headers = {
                        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
                        'cookie': 'channelid=0; sid=1487236586043529; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487237142; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487237142; _ga=GA1.2.312655308.1487237144; _gat=1'
                    }
                )
            except Exception as e:
                print(str(e))
                print('request again')

    def crawl_per_page(self,page_index):
        print('---------- page {}  ------------'.format(page_index))
        page_url = '{}/{}'\
            .format(self.first_page_url,page_index)
        parser = Parser(html_source=self.own_rq(page_url).text)
        for sec in parser.get_sections():
            server = KuaiProxyServer(sec)
            server.save_to_db()
            server.show_in_cmd()

    def run(self,thread_cot=64):
        pool = ThreadPool(thread_cot)
        page_range = range(1,self.page_num)
        print(page_range)
        pool.map(self.crawl_per_page,page_range)


if __name__=="__main__":
    KuaiSpider(url='http://www.kuaidaili.com/free/outtr').run()