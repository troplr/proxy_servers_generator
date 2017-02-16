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
import time
import random
import requests
from db_config import Session,engine
from models import ProxyServerORM
from sqlalchemy import text
from multiprocessing.dummy import Pool as ThreadPool
from Timer import get_beijing_time

class UpdateModel:
    db_session = Session()

    def get_limit_proxy_servers(self,limit):
        servers = self.db_session.query(ProxyServerORM).filter(
            text("check_in_this_session is not True "
                 " order by id {} limit :limit"\
                 .format(random.choice(['','desc'])))
        ).params(limit=limit).all()
        return servers

    def test_if_ok(self,proxy_server):
        if 'socks4/5' in proxy_server.type:
            port_type = 'socks5'
        else:
            port_type = proxy_server.type.lower()
        proxy_url = "{}://{}:{}".format(
            port_type,
            proxy_server.ip,
            proxy_server.port
        )
        #print(proxy_url)
        proxies = {
            "http": proxy_url,
            "https": proxy_url
        }
        try:
            r = requests.get(
                url = "https://www.google.com/",
                proxies = proxies,
                timeout = 10,
                #verify = False
            )
            print('\n{} test Success: {}\n'.format(proxy_url,r.text))
            return r.text
        except Exception as e:
            #print(str(e))
            print('{} test ERROR '.format(proxy_url))
            return False

    def mark_test_result(self,proxy_server,test_result):
        '''
        if proxy_server.fail_cot > 5:
            self.db_session.delete(proxy_server)
        '''
        proxy_server.check_in_this_session = True
        proxy_server.last_check_time = get_beijing_time()
        if test_result==False:
            proxy_server.fail_cot += 1
        else:
            proxy_server.fail_cot -= 1

    def alter_server(self,proxy_server):
        result = self.test_if_ok(proxy_server)
        self.mark_test_result(proxy_server,result)
        return True if result else False

    def open_new_test_session(self):
        conn = engine.connect()
        conn.execute(
            'update proxy_server set check_in_this_session=FALSE '
        )
        conn.close()

    def run_test(self,limit=512):
        while(1):
            servers = self.get_limit_proxy_servers(limit=limit)
            if len(servers)==0:
                print('the big loop ok! ')
                self.open_new_test_session()
                time.sleep(1)
                continue
            left = 0
            gap = 128
            while(left<limit):
                pool = ThreadPool(128)
                res = pool.map(self.alter_server,servers[left:left+gap])
                try:
                    self.db_session.commit()
                    print('\nSession Commit {} items OK!\n{} servers ping OK!\n'\
                          .format(gap,res.count(True)))
                except Exception as e:
                    print(str(e))
                pool.close()
                pool.join()
                left += gap
            print('--------- Next Loop --------')

if __name__=="__main__":
    UpdateModel().run_test()



