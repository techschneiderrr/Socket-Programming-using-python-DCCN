import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1518

s.bind((host,port))
s.listen(5)
print("The server is now listening.... at host :",host," port :",port)
c,a = s.accept()  # c=>socket , a=> address

while True:
    data = c.recv(1024)
    data = json.loads(data.decode())
    List_a = data.get("a")
    ele = data.get("b")
    asc = List_a
    asc.sort()
    dsc=asc[::-1]
    print("The array is sorted.")
    response = json.dumps({"List_asc":asc, "List_dsc":dsc})
    c.send(response)
c.close()