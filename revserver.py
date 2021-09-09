import socket, sys
s = socket.socket()
host = socket.gethostname()
port = 1512

s.bind((host,port))
s.listen(5)
print("The server is now listening.... at host :",host," port :",port)
c,a = s.accept()
i=0
while i<1:
    i+=1
    usr = c.recv(1024)
    print ("Client : "+usr [::-1])
    msg = raw_input("Enter response to client : ")
    c.send("Server : "+msg)
c.close()