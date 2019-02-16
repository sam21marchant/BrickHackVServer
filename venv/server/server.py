print("Hello")

print("Hi connor")
print("matt is a fool")
print ("matt is a very large fool")
import socket

HOST = ''
PORT = 35002

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind((HOST, PORT))

soc.listen(1)

conn, addr = soc.accept()

print("Connected by ", addr)

while 1:
    data = conn.recv(1024)
    print("recieved by client ", data)
    if not data: break

    conn.sendall(data)
conn.close()

