import socket

myp=socket.SOCK_DGRAM

afn=socket.AF_INET

s=socket.socket(afn,myp)

ip="192.168.1.4"

port=1234

s.bind((ip,port))

x=s.recvfrom(1024)
print(x)


