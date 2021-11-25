import socket, sys, json
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
s = socket.socket()
host = socket.gethostname()
port = 5678
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

while True:
    rows = int(input("\nEnter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))
    print("\nEnter the elements of Matrix:")
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
    print("\n-------------- Enter another matrix --------------")
s.close()
