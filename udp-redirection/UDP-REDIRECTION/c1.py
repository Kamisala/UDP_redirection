# virtual box client
import time
from socket import socket, AF_INET, SOCK_STREAM, SOL_SOCKET, SO_REUSEADDR, SOCK_DGRAM

other_port = 21000
other_ip = '10.0.2.3'


def client_tcp():
    while True:
        try:
            serverName = other_ip
            port = other_port
            serverPort = port

            clientSocket = socket(AF_INET, SOCK_STREAM)
            clientSocket.setsockopt(SOL_SOCKET, SO_REUSEADDR, 1)
            clientSocket.connect((serverName, serverPort))
            msg = 'Hi, I am Client'
            for i in range(5):
                clientSocket.send(msg.encode())
                mssg = clientSocket.recv(1024)
                print(mssg.decode())

            time.sleep(3)
            clientSocket.close()
            print('over')
            break


        except Exception as e:
            time.sleep(1)
            # print('try to connect')
            pass


def client_udp():
    while True:
        server_name = other_ip
        server_port = other_port
        try:
            clientSocket = socket(AF_INET, SOCK_DGRAM)
            #print(time.time())

            for i in range(10):
                message = "Hi,I am Client "+ str(i)
                clientSocket.sendto(message.encode(), (server_name, server_port))
                time.sleep(1)
                message = clientSocket.recv(20480)
                print(message.decode())

            time.sleep(3)
            break
        except Exception as e:
            time.sleep(1)
            pass


if __name__ == '__main__':
    # client_tcp()
    client_udp();

