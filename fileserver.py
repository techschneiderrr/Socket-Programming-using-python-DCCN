import socket

s = socket.socket()
port = 6008
host = socket.gethostname()
s.bind((host, port))
s.listen(5)

print('Server listening ....')

while True:
    conn, addr = s.accept()
    print('\nGot connection from', addr)
    data = conn.recv(1024)
    print('Server recieved', repr(data))

    filename = './my.txt'
    f = open(filename, 'rb')
    l = f.read(1024)
    while(1):
        conn.send(l)
        print('Sent', repr(1))
        l = f.read(1024)
        break
    f.close()

    print('Done sending')
    conn.send('Thankyou for connecting')
    conn.close()
