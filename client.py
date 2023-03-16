import socket
import sys
HOST = '127.0.0.1'
PORT = 1234
client = socket.socket(socket.AF_INET, socket.SOCK_STREAM)

client.connect((HOST, PORT))


try:
    while True:
            data = client.recv(4096).decode().strip('\n')
            buffer = input("<shell>"+data+">")
            buffer += '\n'
            client.send(buffer.encode())
            response = client.recv(4096)
            print(response.decode())
except KeyboardInterrupt:
    print('User terminated.')
    client.close()
    sys.exit()