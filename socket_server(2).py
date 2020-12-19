#！/usr/bin/env python    
#coding:utf-8
import sys,socket,signal
#开启ip和端口
ip_port = ('192.168.130.63',9999)
#生成一个句柄
sk = socket.socket()
#绑定ip端口
sk.bind(ip_port)
#最多连接�
running = True
def handler(signal,frame):
    global running
    print("CTRL C...exiting")
    running=False
    sys.exit(0)

signal.signal(signal.SIGINT,handler)

sk.listen(5)
#开启死循环
while(running):
 
    print ('server waiting...')
    #等待链接,阻塞，直到渠道链接 conn打开一个新的对象 专门给当前链接的客户端 addr是ip地址
    conn,addr = sk.accept()
    #获取客户端请求数据
    while(True):
        client_data = conn.recv(1024)
        #打印对方的数据
        print('Received %s command:'%addr[0]+str(client_data,'utf8'))
        #向对方发送数据
        conn.sendall(bytes('Received %s command:'%addr[0]+str(client_data,'utf8'),'utf8'))
        if(str(client_data,'utf8')=='exit'):
            print('Client exit')
            break

    #关闭链接
    conn.close()
