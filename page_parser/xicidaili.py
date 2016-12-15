#coding:utf-8
"""
@file:      xicidaili
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-12-13 9:34
@description:
            parser for http://www.xicidaili.com/wt/3
"""

from proxy_server_class import ProxyServer
from bs4 import BeautifulSoup

class Parser:
    def __init__(self,html_source):
        self.soup = BeautifulSoup(
                html_source,'html.parser')
        #print(self.soup)

    def get_sections(self):
        return self.soup.select('#ip_list > tr')[1:]

    def get_page_num(self):
        return self.soup.select('.pagination > a')[-2].text

class XiCiProxyServer(ProxyServer):
    def __init__(self,html_section):
        ProxyServer.__init__(self)
        for t_name in ['th','td']:
            self.tds = html_section.find_all(t_name)
            if self.tds:
                break
        #print(self.tds)
        self.generate_all_method()

    def generate_ip(self):
        self.ip = self.tds[1].text.strip()

    def generate_port(self):
        self.port = int(self.tds[2].text.strip())

    def generate_location(self):
        self.location = self.tds[3].text.strip()

    def generate_is_anonymous(self):
        self.is_anonymous = False if self.tds[4].text=='透明' else True

    def generate_type(self):
        self.type = self.tds[5].text.strip()


if __name__=="__main__":
    import requests
    parser = Parser(html_source=requests.get(
        url = 'http://www.xicidaili.com/wt/3',
        headers = {
            'User-Agent': 'Mozilla/5.0 (Windows NT 10.0; WOW64) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/55.0.2883.75 Safari/537.36'
        }
    ).text)

    for sec in parser.get_sections():
        #print(sec)
        XiCiProxyServer(html_section=sec).show_in_cmd()