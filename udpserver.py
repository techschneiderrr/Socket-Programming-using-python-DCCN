import socket

localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024

msgFromServer = "hello UDP client"
bytesToSend = str.encode(msgFromServer)

#create a datgram socket
udpServerSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)

#bind address and ip
udpServerSocket.bind((localIP, localPort))

print("UDP server up and listening")

#listen for incoming datagrams
while True:
    bytesAddressPair = udpServerSocket.recvfrom(bufferSize)
    message = bytesAddressPair[0]
    addr = bytesAddressPair[1]
    print("The message is : ",message)
    print("The client IP is : ",addr)

    #sending reply to client
    udpServerSocket.sendto(bytesToSend,addr)
