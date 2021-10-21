import socket , sys, json
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),5678))
s.listen(5)
print('\nServer is now listening...')
while True:
    ctrl,addr = s.accept()
    output = 'Thankyou for connecting'
    ctrl.send(output.encode())
    data = ctrl.recv(1024)
    data = json.loads(data.decode())
    def_direc=[]
    directory = data.get("a")
    name = data.get("b")
    def_direc.extend(directory)
    for i in range(0,len(def_direc)):
        if(def_direc[i]["name"].find(name)!=-1):
            print(def_direc[i]["phone"])
            response = str(def_direc[i]["phone"])
            ctrl.send(response)
    ctrl.close()