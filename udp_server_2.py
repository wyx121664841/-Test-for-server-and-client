import socket  #套接字类
import numpy as np
import time
PORT = 9999    #端口
##两类基于文件的家族名：AF_UNIX      面向网络的家族名：AF_INET   TCP套接字的名字SOCK_STREAM     UDP套接字的名字SOCK_DGRAM
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
client_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
#生成一个句柄：缩写形式 sk = socket.socket()
#请求连接服务端sk.connect(ip_port)  #套接字捆绑
##ip_port = ('10.150.25.39',9999)   #所需要连接的服务器ip和端口
address = ("192.168.56.1", PORT)
server_socket.bind(address)  #套接字捆绑地址
receive_data_array = []
# while True:   #创建连接=1
for i in range(3):
    print('server waiting for love')
    # 接收客户端传来的数据 recvfrom接收客户端的数据，默认是阻塞的，直到有客户端传来数据
    # recvfrom 参数的意义，表示最大能接收多少数据，单位是字节
    # recvfrom返回值说明
    # receive_data表示接受到的传来的数据,是bytes类型, receive_data.decode()解码，将bytes类型转换为字符串类型
    # client_address 表示传来数据的客户端的身份信息，客户端的ip和端口，元组
    # receive_data, client = server_socket.recvfrom(1024)
    # receive_data = [1, 11, 12]
    # for i in range(3)
    # receive_data1 = [3, 14, 15]
    # receive_data2 = [2, 6, 6]
    receive_data, client_address = server_socket.recvfrom(1024)
    # for i in range(1):
              # time.sleep(5)
    receive_data_array.append(receive_data.decode())
            # receive_data_array.append(receive_data)
            # receive_data_array.append(receive_data1)
            # receive_data_array.append(receive_data2)

            # print(receive_data_array)
            #
            # if not receive_data: break

    # print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))
    print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))

    # server_address = ("192.168.56.1", 9999)
    #
    # msg = input("请输入：")
    # server_socket.sendto(msg.encode(), client_address)
    # server_reply,server_address=client_socket.recvfrom(1024)
    # 打印接受的数据
    # print(str(server_reply, 'utf8'))
    # if (msg == 'quit'):
    #     break

    print(receive_data_array)
    # if i > 3 :
    #     break
    #     break
# for j in range(4):
# receive_data_array = np.array(receive_data_array)
msg = input("请输入检索设备：")
# if (msg == receive_data_array[0][0]):
if (msg == '1'):
        print(receive_data_array[0])  #打印第一行去除第一标识符坐标
        # print(receive_data_array)
        # receive_data_array1 = []
        # server_socket.sendto("hello".encode(), client_address)
elif (msg == '2'):
    print(receive_data_array[1])
        # print(receive_data_array2)
        # receive_data_array2 = []
        # server_socket.sendto("hello".encode(), client_address)
    # else:
    #     server_socket.sendto(msg.encode(), client_address)
elif (msg == '3'):
    print(receive_data_array[2])
# 关闭连接
client_socket.close()