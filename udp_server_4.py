import socket  #套接字类
PORT = 9998    #端口
##两类基于文件的家族名：AF_UNIX      面向网络的家族名：AF_INET   TCP套接字的名字SOCK_STREAM     UDP套接字的名字SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#生成一个句柄：缩写形式 sk = socket.socket()
#请求连接服务端sk.connect(ip_port)  #套接字捆绑
##ip_port = ('10.150.25.39',9999)   #所需要连接的服务器ip和端口
address = ("192.168.56.1", PORT)
server_socket.bind(address)  #套接字捆绑地址
while True:   #创建连接=1
    print('server waiting for love')
    # 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
    # recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
    # recvfrom返回值说明
    # receive_data表示接受到的传来的数据,是bytes类型, receive_data.decode()解码，将bytes类型转换为字符串类型
    # client_address 表示传来数据的客户端的身份信息，客户端的ip和端口，元组
    # receive_data, client = server_socket.recvfrom(1024)
    receive_data, client_address = server_socket.recvfrom(1024)
    # print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))
    print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))

    server_address = ("192.168.56.1", 9999)

    msg = input("请输入：")
    server_socket.sendto(msg.encode(), client_address)
    # server_reply,server_address=client_socket.recvfrom(1024)
    # 打印接受的数据
    # print(str(server_reply, 'utf8'))
    if (msg == 'quit'):
        break
# 关闭连接
client_socket.close()