'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-11-16 09:15:50
LastEditors: lishaogang
LastEditTime: 2021-11-16 09:23:27
'''
import random

def test_sort(func):
    arr = [random.randint(0,20) for _ in range(random.randint(10,30))]
    func(arr)
    print(arr)
