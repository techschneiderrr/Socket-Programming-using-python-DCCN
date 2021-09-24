import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1517
s.connect((host, port))

while True:
    usr = raw_input("Enter message to server : ")
    s.sendall(usr)

    data = s.recv(1024)
    print(data)

    print("\n-------------- Check another string --------------")
   
s.close()
