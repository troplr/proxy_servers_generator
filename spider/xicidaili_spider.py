#coding:utf-8
"""
@file:      xicidaili_spider.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-12-15 14:18
@description:

"""

from page_parser.xicidaili import Parser,XiCiProxyServer
from multiprocessing.dummy import Pool as ThreadPool
import requests

class XiCiSpider:
    """
        sample url: http://www.xicidaili.com/wt/1
    """
    def __init__(self,url):
        parser = Parser(
            html_source = self.own_rq(url).text
        )
        self.page_num = parser.get_page_num()
        print(self.page_num)
        self.type2 = url.split('/')[-2]
        print(self.type2)

    def own_rq(self,url):
        for i in range(10):
            try:
                return requests.get(url,
                        headers = {
                            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
                        }
                    )
            except Exception as e:
                print(str(e))
                print('request again')


    def crawl_per_page(self,page_index):
        print('---------- page {}  ------------'.format(page_index))
        page_url = 'http://www.xicidaili.com/{}/{}'\
            .format(self.type2,page_index)
        parser = Parser(html_source=self.own_rq(page_url).text)
        for sec in parser.get_sections():
            server = XiCiProxyServer(sec,
                type2 = self.type2
            )
            server.save_to_db()
            server.show_in_cmd()

    def run(self,thread_cot=64):
        pool = ThreadPool(thread_cot)
        page_range = range(1,self.page_num)
        print(page_range)
        pool.map(self.crawl_per_page,page_range)

if __name__=="__main__":
    XiCiSpider('http://www.xicidaili.com/nn/').run()