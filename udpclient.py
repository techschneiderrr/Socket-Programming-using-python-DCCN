import socket

msgFromClient = input("Enter the message you want to send : ")
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1, 20001")
updClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

updClientSocket.sendto(bytesToSend, serverAddressPort)

msgFromServer = 