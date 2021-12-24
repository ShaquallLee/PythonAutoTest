'''
Descripttion: 装饰器集合
Author: lishaogang
version: 
Date: 2021-12-24 10:08:54
LastEditors: lishaogang
LastEditTime: 2021-12-24 11:31:45
'''
# from _typeshed import Self
import time
from functools import wraps

buffer = []


# 正常无参函数装饰器
def timeit(func):
    @wraps(func)  # 保持被装饰函数的名字不变
    def wrapper(*args, **kwargs):
        start = time.time()
        time.sleep(0.2)
        res = func(*args, **kwargs)
        print(time.time()-start)
        return res
    return wrapper


# 正常无参数类实现的函数装饰器
class Timeit:
    def __init__(self, func) -> None:
        wraps(func)(self)  # 用于保持被装饰函数的函数名，
        # 若是没有上面一行，会返回Timeit类中的__name__属性，若是没有的话，则会报错
        self.__func = func

    def __call__(self, *args, **kwargs):
        start = time.time()
        time.sleep(0.1)
        res = self.__func(*args, **kwargs)
        print(time.time()-start)
        return res


# 函数实现的有参函数装饰器
def timeit2arr(arr):
    def timeit(func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            arr.append(res)
            print(time.time()-start)
            return res
        return wrapper
    return timeit


# 类实现的有参函数装饰器
class Timeit2arr:
    def __init__(self, arr) -> None:
        self.__arr = arr

    def __call__(self, func):
        @wraps(func)
        def wrapper(*args, **kwargs):
            start = time.time()
            res = func(*args, **kwargs)
            self.__arr.append(res)
            print(time.time()-start)
            return res
        return wrapper


@Timeit2arr(buffer)
def my_add(a, b):
    return a+b



def hello(cls):
    class wrapper():
        def __init__(self, *args, **kwargs):
            print("hello, friends!")
            self.__wrap = cls(*args, **kwargs)
        
        def __getattr__(self, name: str):
            return getattr(self.__wrap, name)
        
    return wrapper


@hello
class ADD():
    def __init__(self, a, b) -> None:
        self.__a = a
        self.__b = b

    @property
    def sum(self):
        return self.__a+self.__b


if __name__ == "__main__":
    myadd = ADD(12,14)
    print(myadd.sum)
    # print(my_add(12, 31))
    # print(my_add.__name__)
    # print(buffer)
