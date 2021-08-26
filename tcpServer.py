import socket
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),5679))
s.listen(5)
print('\nServer is now listening...')
while True:
    ctrl,adr = s.accept()
    output = 'Thankyou for connecting'
    ctrl.send(output.encode())
    ctrl.close()