import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1511

s.bind((host,port))
s.listen(5)
print("The server is now listening.... at host :",host," port :",port)
c,a = s.accept()  # c=>socket , a=> address

while True:
    data = c.recv(1024)
    data = json.loads(data.decode())
    matrix_a = data.get("a")
    matrix_b = data.get("b")
    rows = data.get("c")
    column = data.get("d")
    result=[[0 for i in range(column)] for i in range(rows)]
    for i in range(rows):
        for j in range(column):
            result[i][j] = matrix_a[i][j]+matrix_b[i][j]
    print("The Sum of received two Matrices is : ")
    for r in result:
        print(r)
    response = json.dumps({"response":result})
    c.send(response)
c.close()