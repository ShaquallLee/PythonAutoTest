'''
Descripttion: 多线程交替打印ABC
Author: lishaogang
version: 
Date: 2021-12-25 10:39:54
LastEditors: lishaogang
LastEditTime: 2021-12-25 10:47:41
'''
import threading
import time

def A():
    for i in range(10):
        lockc.acquire()
        print('A', end="")
        time.sleep(0.2)
        locka.release()
    # print("A is end")

def B():
    for i in range(10):
        locka.acquire()
        print('B', end='')
        time.sleep(0.2)
        lockb.release()
    # print("B is end")

def C():
    for i in range(10):
        lockb.acquire()
        print('C', end='')
        time.sleep(0.2)
        lockc.release()
    # print("C is end")


if __name__ == "__main__":
    locka = threading.Lock()
    lockb = threading.Lock()
    lockc = threading.Lock()

    threada = threading.Thread(target=A)
    threadb = threading.Thread(target=B)
    threadc = threading.Thread(target=C)

    lockb.acquire()
    locka.acquire()

    threada.start()
    threadb.start()
    threadc.start()

    threadc.join()

    print("\nending……")
    