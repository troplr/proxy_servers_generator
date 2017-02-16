#coding:utf-8
"""
@file:      test_kuaidaili
@author:    lyn
@contact:   tonylu716@gmail.com
@python:    3.3
@editor:    PyCharm Mac
@create:    2017/2/16 20:16
@description:
            --
"""

import requests

resp = requests.get(
    url = 'http://www.kuaidaili.com/free/outha/349',
    headers = {
        'cookie': 'channelid=0; sid=1487245785393826; _ga=GA1.2.312655308.1487237144; _gat=1; Hm_lvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487237142; Hm_lpvt_7ed65b1cc4b810e9fd37959c9bb51b31=1487248182',
        'User-Agent': 'Mozilla/5.0 (Macintosh; Intel Mac OS X 10_12_3) AppleWebKit/537.36 (KHTML, like Gecko) Chrome/56.0.2924.87 Safari/537.36',
    }
).text

print(resp)