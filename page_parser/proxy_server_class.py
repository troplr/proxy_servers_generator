#coding:utf-8
"""
@file:      proxy_server_class
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-12-13 9:36
@description:
            proxy server 基类
"""

class ProxyServer:
    ip = None
    port = None
    type = None
    is_anonymous = None
    location = None

    def generate_ip(self):
        pass

    def generate_port(self):
        pass

    def generate_location(self):
        pass

    def generate_is_anonymous(self):
        pass

    def generate_type(self):
        pass

    def generate_all_method(self):
        self.generate_ip()
        self.generate_port()
        self.generate_location()
        self.generate_is_anonymous()
        self.generate_type()

    def save_to_db(self):
        pass

    def show_in_cmd(self):
        print('\n---------- New Proxy Server ---------------')
        print('ip:\t\t{}'.format(self.ip))
        print('port:\t{}'.format(self.port))
        print('type:\t{}'.format(self.type))
        print('is_anonymous:\t{}'.format(self.is_anonymous))
        print('location:\t\t{}'.format(self.location))
