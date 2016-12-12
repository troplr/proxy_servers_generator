#coding:utf-8
"""
@file:      proxy_server_orm
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm
@create:    2016-12-12 19:08
@description:
            代理服务器的数据库对象
"""
from sqlalchemy import (
    Column, Integer,
    String, DateTime,Boolean,
)

from sqlalchemy.ext.declarative import declarative_base
Base = declarative_base()

class ProxyServer(Base):
    id = Column(Integer,primary_key=True,autoincrement=True)
    ip = Column(String)
    port = Column(Integer)
    location = Column(String)
    is_anonymous = Column(Boolean)
    type = Column(String)
    last_check_time = Column(DateTime)

    def __init__(self,table_name='proxy_server'):
        self.__tablename__ = table_name

    def __repr__(self):
        return (
            "<ProxyServer(ip={},port={},location={})>"
        ).format(self.ip,self.port,self.location)