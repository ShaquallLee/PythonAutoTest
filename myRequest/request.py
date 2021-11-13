'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-13 15:20:15
LastEditors: lishaogang
LastEditTime: 2021-11-13 15:40:04
'''

import requests

url = r"http://www.baidu.com"

req = requests.get(url=url)
print(req.content)