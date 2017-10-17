#coding=utf-8
#!/usr/bin/env python
'''
author:Mr.Jing
created on Fri Sep 22 14:29:03 2017
platfrom:win10,python2.7
'''

from socket import *
from time import  ctime
import  threading
import time
HOST='127.0.0.1'
PORT=8888
BUFSIZ=1024
ADDR = (HOST,PORT)

tcpSerSock=socket(AF_INET,SOCK_STREAM)
tcpSerSock.bind(ADDR)
tcpSerSock.listen(5)
socks=[]                             #放每个客户端的socket

def handle():
    while True:
        for s in socks:
            try:
                data = s.recv(BUFSIZ)     #到这里程序继续向下执行
            except Exception, e:        
                continue
            if not data:
                socks.remove(s)
                continue
            s.send('[%s],%s' % (ctime(), data))  

t = threading.Thread(target=handle)             #子线程
if __name__ == '__main__':
    t.start()
    print  u'我在%s线程中 ' % threading.current_thread().name    #本身是主线程
    print 'waiting for connecting...'
    while True:
        clientSock,addr = tcpSerSock.accept()
        print  'connected from:', addr
        clientSock.setblocking(0)
        socks.append(clientSock)