import socket
import threading
import time

def main():

    PYPORT = 5803
    PYIP = "192.168.0.35"
    server_socket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
    server_socket.bind((PYIP, PYPORT))

    server_socket.listen(5)
    print("TCPServer Waiting for client on port " + str(PYPORT))

    while True:

        # 클라이언트 요청 대기중 .
        client_socket, address = server_socket.accept()
        # 클라이언트 호스트네임
        # 연결 요청 성공

        data = client_socket.recv(1024)
        print(data.decode(), address)
        print(data.decode())
        if data.decode()=="start":
            data = client_socket.recv(1024)
            strData = data.decode()
            print("string : ", strData)

            filename = "sample2.jpg"

            start = time.time()
            # senStartStr = "start,"+filename
            senStartStr = "start"
            client_socket.send(senStartStr.encode())

            senStartStr = filename
            client_socket.send(senStartStr.encode())

            # data, addr = server_socket.recvfrom(512)
            # print(data.decode())
            data = client_socket.recv(1024)
            if data.decode() == "go":
                # yoloed_file = open(filename, 'rb')
                with open(filename, 'rb') as yoloed_file:
                    filePack = yoloed_file.read(1024)
                    print('sending....')
                    filesize = 0
                    while filePack:
                        filesize += client_socket.send(filePack)
                        filePack = yoloed_file.read(1024)
                    time.sleep(5)
                client_socket.send("end".encode())

            print("********** : ", time.time() - start)
            print("filesize : ", filesize)

            # filePack.close()


main()
