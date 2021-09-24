import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1517

s.bind((host,port))
s.listen(5)
print("The server is now listening.... at host :",host," port :",port)
c,a = s.accept()  # c=>socket , a=> address

while True:
    usr = c.recv(1024)
    test_str = usr
  


    print("Computation done")
    res = {}
    for keys in test_str:
        res[keys] = res.get(keys, 0) + 1
    data = json.dumps({"res": res})
    
    c.send(data)
c.close()