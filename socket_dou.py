import  socket #标准库
ip_port  =  ( '192.168.130.63' , 9998 )  ##声明
sk  =  socket.socket()     ##生成一个句柄缩写缩写
sk.bind(ip_port)# 捆绑play
sk.listen( 5 )     ##同时监听5各队列
while  True :
     print ( 'server waiting...' )
     conn,addr  =  sk.accept()   ##会把客户端的端口和IP，生成一个实例，只为这个客户端服务
##  生成的实例，地址
     client_data  =  conn.recv( 1024 )   ##1024个字节/比特客户端数据大小
     print ( str (client_data, 'utf8' ))  #打印客户端数据
     conn.sendall(bytes( 'Can you hear me？' , 'utf8' ))
     while  True :
         client_data  =  conn.recv( 1024 )
         print ( str (client_data, 'utf8' ))
         server_response  =  input ( "\033[31;1m>>:\033[0m" ).strip()
         conn.send(bytes(server_response, 'utf8' ))
     conn.close()
import  socket
ip_port  =  ( '192.168.130.63' , 9998 )
sk  =  socket.socket()
sk.connect(ip_port)
sk.sendall(bytes( 'Can I hear you？' , 'utf8' ))
server_reply  =  sk.recv( 1024 )
print ( str (server_reply, 'utf8' ))
while   True :
     user_input  = input ( ">>:" ).strip()
     sk.sendall(bytes(user_input, 'utf8' ))
     server_reply  =  sk.recv( 1024 )
     print ( str (server_reply,  'utf8' ))
sk.close()