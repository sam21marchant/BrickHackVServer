import socket
from _thread import *
import threading
print_lock = threading.Lock()

import json

def clientThread(client):
    while True:
        data = client.recv(1024)
        if not data:
            print('bye')
        print_lock.release()
        break
    client.close()

def Main():

    HOST = ''
    PORT = 35002

    soc = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

    soc.bind((HOST, PORT))

    soc.listen(1)
    print("Server is listening")
    while True:
        conn, addr = soc.accept()
        print_lock.aquire()
        print("Connected by ", addr)
        start_new_thread(clientThread, (client,))
    soc.close()
'''
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
'''