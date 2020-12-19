
#！/usr/bin/env python
#coding:utf-8
import socket
#链接服务端ip和端口
# ip_port = ('183.129.176.220',9999)
# ip_port = ('103.46.128.49',9999)
# ip_port = ('183.129.176.220',9999)
ip_port = ('10.150.25.39',9999)
#生成一个句柄
sk = socket.socket()
#请求连接服务端
sk.connect(ip_port)
#发送数据
while(True):
    msg=input("Send your command(exit to quit):")
    sk.sendall(bytes(msg,'utf8'))
    #接受数据
    server_reply = sk.recv(1024)
    #打印接受的数据
    print (str(server_reply,'utf8'))
    if(msg=='exit'):
        break
#关闭连接
sk.close()