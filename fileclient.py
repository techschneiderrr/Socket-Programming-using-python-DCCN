import json
import socket                   # Import socket module
import fileinput
  


def listToString(my_str): 
    
    # initialize an empty string
    str1 = " " 
    
    # return string  
    return (str1.join(my_str))
        

s = socket.socket()             # Create a socket object
host = socket.gethostname()     # Get local machine name
port = 60000                    # Reserve a port for your service.

s.connect((host, port))


with open('received_file', 'wb') as f:
    # print ('file opened')
    while True:
        lst = []
 
        # number of elements as input
        print("Enter number of elements : ")
        print("Writing data to file...")
        print("Sending data to server... ")
        print("Enter number of elements : ")
        # Using fileinput.input() method
        for line in fileinput.input(files ='gfg.txt'):
            print(line)
            
        n = input()
        # iterating till the range
        for i in range(0, n):
            ele = int(input())
            lst.append(ele) # adding the element
     
        string_ints = [str(int) for int in lst]
        strr = ",".join(string_ints)

        s.send(strr.encode())

        print('receiving data...')
        data = s.recv(1024)
        data_loaded = json.loads(data.decode("utf-8")) #data loaded
        print('data=', (data_loaded))
        if not data:
            break
        # write data to a file
        f.write(data)

f.close()
print('Successfully get the file')
s.close()
print('connection closed')