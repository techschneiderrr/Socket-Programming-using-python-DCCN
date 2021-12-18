import socket
import json
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET,
type=socket.SOCK_DGRAM)

def Convert(string):
    li = list(string.split(" "))
    return li

def listToString(s): 
    str1 = " " 
    for ele in s: 
        str1 += ele 
    return str1 

def remove_odd_elements(lst):
    i=0
    for element in lst:
        if i % 2 == 0:
            pass
        else:
            lst.remove(element)
        i = i + 1

print("19BIT0217 - Manav Deep Singh Lamba") 
while True:
    mess = raw_input("Enter message: ")
    lst = Convert(mess)
    remove_odd_elements(lst)
    message = listToString(lst)
    if message == 'exit':
        break
    UDPClientSocket.sendto(message.encode(), serverAddressPort)
    messageFromServer = UDPClientSocket.recvfrom(bufferSize)
    print("Message from Server:{}".format(messageFromServer[0].decode()))