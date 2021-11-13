'''
Descripttion: socket编程客户端代码
Author: lishaogang
version: 1.0
Date: 2021-11-10 10:17:31
LastEditors: lishaogang
LastEditTime: 2021-11-10 12:29:31
'''

import socket
import threading

shut = False

def makeLink(ip, port):
    global shut
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.connect((ip, port))
    soc.settimeout(5)
    shut = False
    return soc

def listenMsg(soc):
    '''
    接收信息'''
    global shut
    while not shut:
        try:
            msg = soc.recv(1024).decode("utf-8")
            print(f'>>>服务端:{msg}')
        except socket.timeout:
            continue
        except:
            print("运行异常结束")
            break

def sendMsg(soc):
    global shut
    while True:
        msg = input()
        soc.send(msg.encode('utf8'))
        if msg=="shutdown":
            shut = True
            break

if __name__ =="__main__":
    ip = "10.62.93.166"
    port = 1999
    soc = makeLink(ip, port)
    print("欢迎使用客户端".center(20,'-'))
    thd_send = threading.Thread(target=sendMsg, args=(soc,))
    thd_recv = threading.Thread(target=listenMsg, args=(soc,))
    thd_send.start()
    thd_recv.start()
    thd_send.join()
    thd_recv.join()
    # soc.close()
    print("运行结束".center(20,'-'))