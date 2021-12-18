import socket
import json
localIP = "127.0.0.1"
localPort = 20002
bufferSize = 1024
UDPServerSocket = socket.socket(family=socket.AF_INET,type=socket.SOCK_DGRAM)
UDPServerSocket.bind((localIP, localPort))
print("UDP server up and listening")
def countTriplets(arr, sum):
    n = len(arr)
    ans = 0
    for i in range( 0 ,n-2):
        for j in range( i+1 ,n-1):
            for k in range( j+1, n):
                if (arr[i] + arr[j] + arr[k] < sum):
                    ans+=1
    return ans
while(True):
    bytesAddressPair = UDPServerSocket.recvfrom(bufferSize)
    array = bytesAddressPair[0]
    array = json.loads(array)
    addr = bytesAddressPair[1]
    print('Got connection from', addr)
    dataArray = array[1:]
    print("Calculating number of possible triplets with sum less than "+str(array[0]))
    result_value = countTriplets(dataArray, array[0])
    print("Number of possible triplets with sum less than "+str(array[0])+" is "+str(result_value))
    print("Sending result back to client")
    UDPServerSocket.sendto(bytes(str.encode(str(result_value))),
addr)