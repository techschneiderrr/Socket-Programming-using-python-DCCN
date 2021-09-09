import socket, sys
s = socket.socket()
host = socket.gethostname()
port = 1512
s.connect((host, port))
i=0
while i<1:
    i+=1
    usr = raw_input("Enter message to server : ")
    s.sendall(usr)
    print(s.recv(1024))
s.close()
