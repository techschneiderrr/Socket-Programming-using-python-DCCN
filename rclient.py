import socket, sys
s = socket.socket
host = socket.gethostname()
port = 5678
s.connect(host, port)
i=0
while i<5:
    i+=1
    usr = raw_input("Enter message : ")
    s.sendall(usr)
    print(s.recv(1024))
s.close()
