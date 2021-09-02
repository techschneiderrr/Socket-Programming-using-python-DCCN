import socket

msgFromClient = input("Enter the message you want to send : ")
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
#creating udp socket at client
updClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)
#send to  server using udp socket created
updClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = updClientSocket.recvfrom(bufferSize)