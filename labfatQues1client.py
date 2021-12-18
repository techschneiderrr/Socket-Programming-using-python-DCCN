import socket
import json
serverAddressPort =("127.0.0.1",20002)
bufferSize = 1024
UDPClientSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
n = int (input("Enter the number of elements in the array: "))
array =[]
array.append(int(input("Enter the value of sum: ")))
for i in range(n):
    array.append(int(input("Enter the element "+ str(i+1)+ ": ")))
input_data = str(array)
UDPClientSocket.sendto(bytes(str.encode(input_data)),serverAddressPort)
answer, addr = UDPClientSocket.recvfrom(bufferSize)
print("Number of triplets with sum less than 12:")
print(json.loads(answer))