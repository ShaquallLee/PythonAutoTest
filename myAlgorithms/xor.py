'''
Descripttion: 异或运算的使用
Author: lishaogang
version: 
Date: 2021-11-14 16:18:20
LastEditors: lishaogang
LastEditTime: 2021-11-14 16:46:02
'''

import time

#在一个数组中有a、b两个数只出现了一次，而其它的数都出现了2次，找出这两个数a和b
def findAB(arr):
    xor = 0
    for x in arr:
        xor ^= x
    
    left_one = xor & (~xor+1)   #从后往前数，找到xor二进制中第一个是1的位

    a = 0
    for x in arr:
        if x&left_one==0:
            a^=x
    return a, xor^a



def testABChangeTime():
    '''测试a、b交换值两种方式所用的时间'''
    start = time.time()
    a = 10
    b=100
    for i in range(1000000):
        a,b=b,a
        # a = a^b
        # b = a^b
        # a = a^b
    print(time.time()-start)

if __name__ == '__main__':
    # arr = [8,1,2,3,5,1,2,5]
    # print(findAB(arr))
    testABChangeTime()
