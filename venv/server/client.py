import socket
import json

HOST = '10.0.0.118'
PORT = 35002

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.connect((HOST, PORT))

while 1:
    stuff = input('enter some stuff: ')
    soc.sendall(stuff.encode())
    if not stuff: break
    data = soc.recv(1024)

    print(data.decode())

soc.close()