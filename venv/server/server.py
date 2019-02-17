import socket
import json


HOST = ''
PORT = 35002

soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

soc.bind((HOST, PORT))

soc.listen(1)

conn, addr = soc.accept()

print("Connected by ", addr)

#while 1:
data = conn.recv(1024).decode()
print("recieved by client ", data)
data.strip('\n')
jsonData = json.loads(data)

print(jsonData["username"])
print(jsonData["password"])

# if not data:
    #break

conn.sendall(json.dumps(jsonData).encode())
conn.close()
