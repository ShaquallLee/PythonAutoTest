'''
Descripttion: requests时cookie的使用
Author: lishaogang
version: 
Date: 2021-11-22 11:15:05
LastEditors: lishaogang
LastEditTime: 2021-11-22 11:51:49
'''
import pytest
import requests

@pytest.mark.skip(reason="只是尝试一下cookie在请求过程中的使用")
def test_cookie():
    url = r"http://localhost"
    data = {"user":"lishao", "password":"12345"}
    res = requests.post(url=url+r"/login", data=data)
    
    cookies = dict(res.cookies)
    headers = {"cookie": f"user={cookies.get('user')}"}
    # 发送请求时将之前获得的cookie放到headers请求头里
    students = requests.get(url=url+r'/showusers', headers=headers)
    
    print(students.json())

@pytest.mark.skip(reason="只是实验一下")
def test_cookie2():
    '''
    直接使用requests.session()对象来维持cookie信息'''
    url = r"http://localhost"
    data = {"user":"lishao", "password":"12345"}

    se = requests.session()
    res = se.post(url=url+r"/login", data=data)
    
    # cookies = dict(res.cookies)
    # headers = {"cookie": f"user={cookies.get('user')}"}
    # 发送请求时将之前获得的cookie放到headers请求头里
    students = se.get(url=url+r'/showusers')#, headers=headers)
    
    print(students.json()) 

if __name__ == "__main__":
    test_cookie2()
    