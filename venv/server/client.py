import socket

HOST = '127.0.0.1'
PORT = 35002

soc = socket.socket(socket.AF_INET,socket.SOCK_STREAM)

soc.connect((HOST, PORT))

while 1:
    stuff = raw_input('enter some stuff: ')
    soc.sendall(stuff)
    if not stuff: break
    data = soc.recv(1024)

    print(data)

soc.close()