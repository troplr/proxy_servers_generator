#coding:utf-8

import os,sys
sys.path.append(os.path.dirname(sys.path[0]))

from .proxy_server_class import ProxyServer
from bs4 import BeautifulSoup

class Parser:
    def __init__(self,html_source):
        self.soup = BeautifulSoup(
                html_source,'html.parser')

    def get_sections(self):
        return self.soup.select('tbody > tr') 

    def get_page_num(self):
        try:
            return int(self.soup.find(id="listnav")\
                    .select('li')[-2].text)
        except AttributeError:
            return 1500


class KuaiProxyServer(ProxyServer):
    def __init__(self,html_section):
        ProxyServer.__init__(self)
        self.tds = html_section.find_all('td')
        self.generate_all_method()

    def generate_ip(self):
        self.ip = self.tds[0].text.strip()

    def generate_port(self):
        self.port = self.tds[1].text.strip()

    def generate_is_anonymous(self):
        self.is_anonymous = self.tds[2].text.strip()=='高匿名'

    def generate_type(self):
        self.type = self.tds[3].text.strip()

    def generate_location(self):
        self.location = self.tds[4].text.strip()


if __name__=="__main__":
    with open('./kuaidaili.html') as f:
        html_source = f.read()
    print(html_source)
    parser = Parser(html_source)
    secs = parser.get_sections()
    print(secs,len(secs))

    pages = parser.get_page_num()
    print(pages)

    for sec in secs:
        server = KuaiProxyServer(sec)
        server.show_in_cmd()
