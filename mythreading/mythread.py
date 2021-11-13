'''
Descripttion:threading的使用，多线程 
Author: lishaogang
version: 
Date: 2021-11-09 17:15:56
LastEditors: lishaogang
LastEditTime: 2021-11-09 17:22:27
'''

import threading, time

n = 0
lock = threading.Lock() # 声明一个锁

def thread1():
    global n
    for i in range(1000000):
        lock.acquire() #获取锁
        n+=1
        n-=1
        lock.release()  # 释放锁
    print(n)

if __name__ == "__main__":
    thd1 = threading.Thread(target=thread1)
    thd2 = threading.Thread(target=thread1)
    start = time.time()
    thd1.start()
    thd2.start()
    thd1.join()
    thd2.join()
    print(time.time()-start)