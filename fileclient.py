import socket

s = socket.socket()
host = socket.gethostname()
port = 6008

s.connect((host, port))
s.send("hello server!")

with open('received_file', 'wb') as f:
    print('file opened')
    while True:
        data = s.recv(1024)
        if not data:
            break
        print('receiving data...')
        print('data = ',(data))
        f.write(data)
f.close()