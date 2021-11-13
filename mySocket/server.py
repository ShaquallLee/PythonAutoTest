'''
Descripttion: socket编程服务端代码
Author: lishaogang
version: 1.0
Date: 2021-11-10 09:50:11
LastEditors: lishaogang
LastEditTime: 2021-11-10 12:38:37
'''

import socket
import threading
import time

shut = False
# lock = threading.Lock()

def makeServer(ip, port):
    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    soc.bind((ip, port))
    soc.listen(2)
    return soc


def listenMsg(client, addr):
    '''
    接收信息'''
    global shut
    while not shut:
        try:
            msg = client.recv(1024).decode("utf-8")
            if msg == "shutdown":
                # client.send(msg.encode('utf8'))
                shut = True
                break
            print(f'>>>{addr}:{msg}')
        except socket.timeout:
            continue

def sendMsg(client):
    global shut
    while not shut:
        try:
            msg = input()
            client.send(msg.encode('utf8'))
        except socket.timeout:
            continue

if __name__ == "__main__":
    ip = "10.62.93.166"
    port = 1999
    soc = makeServer(ip, port)
    print("服务端启动".center(20,'*'))
    client, addr = soc.accept()
    client.settimeout(5)
    print(f'>>>{addr}已连接')
    thd_send = threading.Thread(target=sendMsg, args=(client,))
    thd_recv = threading.Thread(target=listenMsg, args=(client, addr,))
    thd_send.start()
    thd_recv.start()
    thd_send.join()
    thd_recv.join()
    # client.close()
    client.shutdown(2)
    client.close()
    print("运行结束".center(20,'*'))

