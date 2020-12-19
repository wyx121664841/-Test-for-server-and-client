import socket
import os
from multiprocessing import Process
PORT = 9999
server_socket = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
address = ("192.168.56.1", PORT)
server_socket.bind(address)

while True:
    receive_data, client_address = server_socket.recvfrom(1024)
    print("receive from %s data: %s" % (client_address, receive_data.decode()))

    if(str(receive_data,'utf8')=='quit'):
       print('client exit')
       break
    #print('hello')

    msg=input('input your comand:')
    server_socket.sendto(bytes(msg.encode()),client_address,)


server_socket.close()
