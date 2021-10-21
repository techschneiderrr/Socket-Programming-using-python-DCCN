import socket, json, sys
from signal import signal, SIGPIPE, SIG_DFL
signal(SIGPIPE,SIG_DFL) 
host = socket.gethostname()
port = 5678
s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.connect((host,port))

n=int(input("Enter total no of records to be entered:-"))
tele=[]
for i in range(0,n):
 dict={}
 username=raw_input("Enter name of emplyoee=")
 dict["name"]=username
 list=[]
 telephoneNo=int(raw_input("how many mobile no a employee has:-"))
 for j in range(0,telephoneNo):
    phoneNo=int(raw_input("Enter phone number:-"))
    list.append(phoneNo)
    dict["phone"]=list
    tele.append(dict)

search=raw_input("\nEnter name to search:-")


while True :
    data = json.dumps({"a": tele,"b": search})
    s.send(data.encode())
    msg = s.recv(4096)
    print(msg.decode())
