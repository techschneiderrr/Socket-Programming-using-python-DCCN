import socket, sys, json
s = socket.socket()
host = socket.gethostname()
port = 1518
s.connect((host, port))

while True:
    ele = int(input("\nEnter the Number of elements : " ))
    print("\nEnter the elements : ")
    List_a= [int(input()) for i in range(ele)]
    print("\nArray entered is : ")
    print(List_a)
    data = json.dumps({"a": List_a, "b": ele})
    s.send(data.encode())
    
    res = s.recv(1024)
    res = json.loads(res)

    asc = res.get("List_asc")
    dsc = res.get("List_dsc")
    print("\nAscending order : ")
    print(asc)
    print("\ndescending order : ")
    print(dsc)
    print("\n-------------- SORT ANOTHER ARRAY --------------")
s.close()
