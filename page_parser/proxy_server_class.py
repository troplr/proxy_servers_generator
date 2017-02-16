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
from models import ProxyServerORM
from db_config import Session
from sqlalchemy.exc import IntegrityError

class ProxyServer:
    def __init__(self):
        self.ip = None
        self.port = None
        self.type = None
        self.type2 = None
        self.is_anonymous = None
        self.location = None

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
        db_session = Session()
        db_session.add(
            ProxyServerORM(
                ip = self.ip,
                port = self.port,
                location = self.location,
                type = self.type,
                type2 = self.type2,
                is_anonymous = self.is_anonymous,
                fail_cot = 0
            )
        )
        try:
            db_session.commit()
            return True
        except IntegrityError as e:
            print(str(e))
        db_session.close()

    def show_in_cmd(self):
        print('\n{}\t{}\t{}\t{}\t{}\t{}'\
              .format(self.ip,self.port,self.type,self.type2,\
                      self.is_anonymous,self.location))