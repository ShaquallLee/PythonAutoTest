'''
Descripttion: 登录接口测试
Author: lishaogang
version: 
Date: 2021-11-18 17:07:03
LastEditors: lishaogang
LastEditTime: 2021-11-19 16:54:09
'''
import sys
sys.path.append('F:\githubfiles\PythonAutoTest')


import requests
import re, json
import pytest
from testInterface.common.utils import *

data = readCsv(data_path+'/login.csv')


@pytest.mark.skipif(data[5][1] != 'Y' and data[5][1] != 'y', reason='此版本不执行该用例')
@pytest.mark.parametrize('info', data[7:8])
def testLogin(info):
    print('测试'+info[0])
    pattern = r'account=(.*)，\npassword=(.*)'
    res = re.findall(pattern, info[1])
    # print(res)
    if res==[]:
        print('not match')
    else:
        das = {}
        das["user"]=res[0][0]
        das["password"]=res[0][1]
        req = request(data[1][1], data[2][1], data=das).json()
        assert req["code"]==info[2] and req["message"]==info[3]


if __name__ == '__main__':
    pytest.main(['-s', __file__])
