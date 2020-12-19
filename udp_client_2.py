#！/usr/bin/env python
#coding:utf-8
import socket
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)

while True:
    msg = input("请输入要发送的内容：")
    server_address = ("192.168.56.1", 9993)
    client_socket.sendto(msg.encode(), server_address)
    server_reply,server_address=client_socket.recvfrom(1024)
    # 打印接受的数据
    print(str(server_reply, 'utf8'))
    if (msg == 'quit'):
        break
# 关闭连接
client_socket.close()
