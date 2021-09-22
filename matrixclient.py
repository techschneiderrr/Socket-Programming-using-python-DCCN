import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1511
s.connect((host, port))

while True:
    rows = int(input("\nEnter the Number of rows : " ))
    column = int(input("Enter the Number of Columns: "))
    print("\nEnter the elements of First Matrix:")
    matrix_a= [[int(input()) for i in range(column)] for i in range(rows)]
    print("\nFirst Matrix is: ")
    for n in matrix_a:
        print(n)
    
    print("\nEnter the elements of Second Matrix:")
    matrix_b= [[int(input()) for i in range(column)] for i in range(rows)]
    print("\nSecond Matrix is: ")
    for n in matrix_b:
        print(n)    
    
    data = json.dumps({"a": matrix_a, "b": matrix_b, "c": rows, "d":column})
    s.send(data.encode())
    
    res = s.recv(1024)
    res = json.loads(res)
    result = res.get("response")
    print("\n")
    print("Resultant Matrix is: ")
    for r in result:
        print(r)
    # print(str(result))
    print("\n-------------- ADD ANOTHER 2 MATRICES --------------")
s.close()
