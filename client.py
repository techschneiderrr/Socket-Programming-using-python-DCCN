import socket
host = socket.gethostname()
port = 1234
s = socket.socket()
s.connect((host,port))
s.sendall('Hello, World !!')
data = s.recv(1024)
print('Recieved', repr(data))
print(s.recv(1024))
s.close()