'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-18 17:09:53
LastEditors: lishaogang
LastEditTime: 2021-11-18 19:06:22
'''

import csv, os, json
from _pytest.mark import param

from attr.setters import NO_OP
import requests

base_path = os.path.dirname(os.path.dirname(__file__))
case_path = os.path.join(base_path, 'case')
data_path = os.path.join(base_path, 'data')
report_path = os.path.join(base_path, 'report')

def readCsv(file):
    '''
    读取CSV文件内容'''
    if os.path.exists(file):
        with open(file, mode='r', encoding='utf-8') as f:
            d = csv.reader(f)
            return list(d)
    else:
        return False


def request(url, mode, data=None, header=None):
    '''
    get or post 请求'''
    # print(data)
    rq = requests.session()
    if mode in ['GET', 'Get', 'get']:
        res = rq.get(url=url, params=data, headers=header)
    elif mode in ['POST', 'Post', 'post']:
        res = rq.post(url=url, params=data, headers=header)
    return res