import socket
host = socket.gethostname()
port = 5679
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

data = "Hello, how are you ?"
while True :
    s.send(data.encode())
    msg = s.recv(4096)
    print(msg.decode())
