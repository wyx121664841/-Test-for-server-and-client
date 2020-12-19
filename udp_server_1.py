import socket
from multiprocessing import Process
import sys, os
import time

def my_fun(self):
    try :
        # 变量声明
        PORT = 9999
        server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
        #重复使用绑定信息
        server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        address = ("192.168.56.1", PORT)
        server_socket.bind(address)
        while True:
            print('server waiting')
            receive_data, client_address = server_socket.recvfrom(1024)

            server_socket.sendto(bytes("hello , if you want to exit the dialog,input quit please!".encode('utf-8')),
                             client_address, )
            # if (str(sendto_data, 'utf8')=='1'):
            #           print("接收到了客户端1 %s 传来的数据: %s" % (client_address, receive_data.decode()))
            # if (str(sendto_data, 'utf8') == '2'):
            #           print("接收到了客户端2 %s 传来的数据: %s" % (client_address, receive_data.decode()))
            # if (str(sendto_data, 'utf8') == '3'):
            #     print("接收到了客户端3 %s 传来的数据: %s" % (client_address, receive_data.decode()))






            print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))
            print(receive_data.decode())



            if (str(receive_data, 'utf8') == 'quit'):
                print('client exit')
                break
    finally:
        server_socket.close()


def works(func, arg, worknum):
    proc_record = []

    for i in range(worknum):
        p = Process(target=func, args=(arg,))
        time.sleep(5)
        p.start()

        proc_record.append(p)
    for p in proc_record:

        p.join()


if __name__ == '__main__':
    arg = 5

    procs=2
    #procs = 4   #进程个数
    # works(timetask, arg, procs)

    works(my_fun, arg, procs)



