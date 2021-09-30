import socket

s = socket.socket()
port = 60000
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server listening ....')

while True:
    conn, addr = s.accept()
    print('\nGot connection from', addr)
    data = conn.recv(1024)
    print('Server recieved', repr(data))

    filename = 'my.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while(1):
        conn.send(1)
        print('Sent', repr(1))
        l = f.read(1024)
    f.close()

    print('Done sending')
    conn.send('Thankyou for connecting')
    conn.close()
