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

from parser.xicidaili import Parser
import requests

class XiCiSpider:
    def __init__(self,url):
        parser = Parser(
            html_source = requests.get(url,
                headers = {
                    'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
                }
            ).text
        )
        self.page_num = parser.get_page_num()
        print(self.page_num)


if __name__=="__main__":
    XiCiSpider('http://www.xicidaili.com/wt/1')