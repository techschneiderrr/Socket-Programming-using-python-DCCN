import socket
import json
localIP = "127.0.0.1"
localPort = 20001
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET,
type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
msgCount = 0
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    if msgCount == 10:
        msg = "Client has already sent 10 messages. ERROR. Not accepting 11th Message"
        print(msg)
        msg = msg.encode("utf-8")
        UDPServerSocket.sendto(msg, bytesAddressPair[1])
        continue
    clientMsg = bytesAddressPair[0]
    msgCount = msgCount + 1
    addr = bytesAddressPair[1]
    clientMsg = clientMsg.decode("utf-8")
    print("Message from Client: " + clientMsg)
    serverMsg = raw_input("Enter message for Client: ")
    msg = serverMsg.encode("utf-8")
    UDPServerSocket.sendto(msg, addr)
    