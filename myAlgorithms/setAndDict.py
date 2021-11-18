'''
Descripttion: 测试dict传入简单类型和传入复杂类型的形式
    从下面实验结果可以看出：
        dict\set 传入简单类型时是值传递，改变原来变量的值并不会影响到dict\set中的值
        当传入复杂类型时，如自定义的类，改变原来变量的值，dict\set中的值也会改变，因为
            传入复杂类型时，使用的是引用传递，存储在dict\set中的值的大小只是相应变量
            所在内存地址的大小，而不是变量的大小
Author: lishaogang
version: 
Date: 2021-11-18 10:10:03
LastEditors: lishaogang
LastEditTime: 2021-11-18 10:19:08
'''

class A():
    def __init__(self,a):
        self._a=a


aa = A(12)
b = 12
d = {aa:1, b:2}
print(d ,list(d.keys())[0]._a)

aa._a=123
print(aa._a)
print(d, list(d.keys())[0]._a)