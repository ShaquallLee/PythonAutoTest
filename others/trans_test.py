'''
Descripttion: 
Author: lishaogang
version: 
Date: 2021-12-20 08:11:11
LastEditors: lishaogang
LastEditTime: 2021-12-21 15:47:02
'''

import random
import time
from functools import wraps


def timeit(func):
    @wraps(func)
    def running(*args, **kwargs):
        start = time.time()
        res = func(*args, **kwargs)
        end = time.time()
        print("time use",end-start)
        return res
    return running

class single(object):
    __instance = None

    def __new__(cls, *args, **kwargs):
        if cls.__instance is None:
            cls.__instance = object.__new__(cls)
        return cls.__instance


def merge(arr, left, right):
    x = arr[right]
    i = left
    while i<=right:
        if arr[i]<x:
            arr[i],arr[left] = arr[left], arr[i]
            left+=1
            i+=1
        elif arr[i]>x:
            arr[i],arr[right] = arr[right], arr[i]
            right-=1
        else:
            i+=1
    return left-1, right

@timeit
def sep_sort(arr, left, right):
    if right-left<1:
        return
    
    mid = random.randint(left, right)

    arr[mid], arr[right] = arr[right], arr[mid]

    nl, nr = merge(arr, left, right)
    sep_sort(arr, left, nl)
    sep_sort(arr, nr, right)



@timeit
def sum(a:int,b:int,c:int)->int:
    # print(__file__)
    print(id(a))
    return a+b+c


instances:dict = {}
def singleton(cls):
    def getinstance(*args, **kwargs):
        if not instances.get(cls):
            instance = cls(*args, **kwargs)
            instances[cls] = instance
        instances[cls].refresh(*args, **kwargs)
        return instances[cls]
    return getinstance


@singleton
class A(object):
    _in1 = None
    __in2 = None
    instance = None

    def __init__(self, a):
        self._a = a
        self.b = 123
        self.__c = 12345
    
    def refresh(self, a):
        self._a = a
    # def __new__(cls, *args, **kwargs):
    #     if not cls.instance:
    #         cls.instance = object.__new__(cls)
    #     return cls.instance





if __name__ == "__main__":
    a = A(12)
    print(a._a)

    b = A(13)
    print(a._a, b._a)
    # print(a.instance)
    # print(b.instance)
    x,y,z = "12","1+","14"
    # print(id(x))
    print(sum(x,y,z))

    # arr = [random.randint(0, 100) for i in range(20)]

    # print(arr)
    # sep_sort(arr, 0, 19)
    # print(arr)
