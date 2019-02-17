from bottle import route, run, static_file
import socket
from _thread import *
import threading
import json


class Server(object):
    def __init__(self, host, port):
        self.party_leader = None
        self.user_list = []
        self.host = host
        self.port = port
        self.sock = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        self.sock.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
        self.sock.bind((self.host, self.port))

    '''
    Listens for new connections and creates new threads based on new connections
    '''
    def listen(self):
        self.sock.listen(1)
        print('Waiting for connection')
        while True:
            client, address = self.sock.accept()
            print('Connection received from IP:', address)
            threading.Thread(target=self.listenToClient, args=(client, address)).start()

    '''
    Once a connection is made with the client, wait until they send data
    '''
    def listenToClient(self, client, address):
        size = 1024
        while True:
            try:
                data = client.recv(size)
                if data:
                    data = data.decode()
                    data.strip('\n')
                    json_data = json.loads(data)
                    action = json_data['action']
                    if action == 'login':
                        username = json_data['username']
                        print(username + ' connected!')
                        client.send('Successfully connected\n'.encode())
                        if self.party_leader is None:
                            self.party_leader = username
                            self.user_list.append(username)
                            client.send('{"isPartyLeader":true, "successful":true}\n'.encode())
                        else:
                            if username in self.user_list:
                                client.send('{"isPartyLeader":false, "successful":false, "message":"A user already has that username"}\n'.encode())
                            else:
                                self.user_list.append(username)
                                client.send('{"isPartyLeader":false, "successful":true}\n'.encode())
                    elif action == 'play':
                        print("I am playing a song now")
                    elif action == 'pause':
                        print("I just paused a song")
                    elif action == 'skip':
                        print("I just skipped a song")
                    elif action == 'replay':
                        print("I just replayed a song")
                    else:
                        print("No action")
                else:
                    raise error('Client disconnected')
            except:
                print('Connection failed')
                client.close()
                return False


if __name__ == "__main__":
    Server('', 35002).listen()
