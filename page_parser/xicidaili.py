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

from .proxy_server_class import ProxyServer
from bs4 import BeautifulSoup

class Parser:
    def __init__(self,html_source):
        self.soup = BeautifulSoup(
                html_source,'html.parser')
        #print(self.soup)

    def get_sections(self):
        return self.soup.select('#ip_list > tr')[1:]

    def get_page_num(self):
        return int(self.soup.select('.pagination > a')[-2].text)


class XiCiProxyServer(ProxyServer):
    def __init__(self,html_section,type2):
        ProxyServer.__init__(self)
        self.type2 = type2
        self.is_anonymous = type2 in ['wn','nn']
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

    def generate_type(self):
        self.type = self.tds[5].text.strip()
