import socket, sys, json
msgFromClient = "Hi this is UDP server"
bytesToSend = str.encode(msgFromClient)
serverAddressPort = ("127.0.0.1", 20001)
bufferSize = 1024
#creating udp socket at client
updClientSocket = socket.socket(family=socket.AF_INET, type=socket.SOCK_DGRAM)


while True:
    rows = int(input("\nEnter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))
    print("\nEnter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
    print("\nThe entered matrix is: ")
    for n in matrix_a:
        print(n)

    data = json.dumps({"a": matrix_a,"c": rows, "d":column})
    s.send(data.encode())
    
    res = s.recv(1024)
    res = json.loads(res)
    result = res.get("response")
    print("\n")
    print("Result : ")
    print(result)
    # print(str(result))
    print("\n-------------- ADD ANOTHER 2 MATRICES --------------")
s.close()
