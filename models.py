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

class ProxyServerORM(Base):
    __tablename__ = 'proxy_server'

    id = Column(Integer,
        primary_key=True,autoincrement=True)
    ip = Column(String)
    port = Column(Integer)
    location = Column(String)
    is_anonymous = Column(Boolean)
    type = Column(String)
    type2 = Column(String)
    last_check_time = Column(DateTime)

    def __repr__(self):
        return (
            "<ProxyServerORM(ip={},port={},location={})>"
        ).format(self.ip,self.port,self.location)