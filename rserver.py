import socket, sys
s = socket.socket
host = socket.gethostname()
port = 5678

s.bind(host,port)
s.listen(5)
# print("The server is now listening.... at host :",host," port :",port)
c,a = s.accept()
i=0
while i<5:
    i+=1
    usr = c.recv(1024)
    print (usr)
    c.send(usr+ " server ")
c.close()