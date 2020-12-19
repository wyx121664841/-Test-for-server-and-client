import socket
from multiprocessing import Process
import threading
import sys, os


def my_fun(self):
    try:
        for i in range(10):
            # 变量声明
            PORT = 9998
            server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
            #重复使用绑定信息
            server_socket.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
            address = ("192.168.56.1", PORT)
            server_socket.bind(address)

            receive_data_array1 = []
            receive_data_array2 = []
            for i in range(2):
                print('server waiting')
                receive_data, client_address = server_socket.recvfrom(1024)
                print("接收到了客户端 %s 传来的数据: %s" % (client_address, receive_data.decode()))

                receive_data_array =[]
                receive_data_array.append(receive_data.decode())
                receive_data_array1 = receive_data_array1 + receive_data_array
                receive_data_array2 = receive_data_array2 + receive_data_array

            msg = input("请输入检索设备：")
            if(msg==(receive_data_array1[0][0:1])):
                    print(receive_data_array1[0])
                    receive_data_array1 = []
                    # server_socket.sendto("hello".encode(), client_address)
            elif(msg==(receive_data_array1[1][0:1])):
                    print(receive_data_array1[1])
                    receive_data_array2 = []
                    # server_socket.sendto("hello".encode(), client_address)
            else:
                    # print(receive_data_array)
                    # server_socket.sendto(msg.encode(), client_address)
                    # print(receive_data_array)
                    print(receive_data_array1)
                    # print(receive_data_array2)
                    # print(receive_data_array3)

    finally:
            server_socket.close()

#进程学习
def process_works(func, arg, worknum):
    proc_record = []
    for i in range(worknum):
        p = Process(target=func, args=(arg,))
        p.start()
        proc_record.append(p)
    for p in proc_record:
        p.join()
#线程学习
def thread_works(func, arg, worknum):
    thread_record = []
    for i in range(worknum):
        t = threading.Thread(target=func, args=(arg,))
        t.start()
        thread_record.append(t)
        print(thread_record)
    for t in thread_record:
        t.join()




if __name__ == '__main__':
    arg = 5
    procs=3
    thread_num=3
    #procs = 2   #进程个数
    #process_works(my_fun, arg, procs)
    thread_works(my_fun, arg, thread_num)
    #process_works(my_fun, arg, worknum):


