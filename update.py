#coding:utf-8
"""
@file:      update.py
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-12-12 19:12
@description:
            负责长期维护代理池，包括测试可用性，增删代理数据表等
"""
import requests


class UpdateModel:
    def __init__(self,proxy_server_query_set):
        self.proxy_servers = proxy_server_query_set

    def test_if_ok(self,proxy_server):
        proxy_url = "{}://{}:{}".format(
            proxy_server.type.lower(),
            proxy_server.ip,
            proxy_server.port
        )
        print(proxy_url)
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        r = requests.get(
            url="https://api.ipify.org/",
            proxies=proxies,
            timeout=20,
        )
        return r.text

    def run_test(self):
        for proxy_server in self.proxy_servers:
            self.test_if_ok(proxy_server)

if __name__=="__main__":
    from models.ProxyServerORM import ProxyServerORM
    UpdateModel(
        
    )

