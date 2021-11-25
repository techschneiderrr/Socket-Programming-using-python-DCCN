import socket, sys, json, math

s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
s.bind((socket.gethostname(),5678))
s.listen(5)
c,a = s.accept()  # c=>socket , a=> addres
def sumAlternate(arr, n):
    sum1 = 0
    sum2 = 0
    alt = 0
 
    i = 0
    while i < n * n :
 
        # count the elements at
        # even places
        if (i % 2 == 0):
            sum1 += math.factorial(arr + i)
 
        else: # count the elements
              # at odd places
            sum2 += math.factorial(arr + i)
             
        i += 1
    alt = str(sum2)
    return alt
while True:
    data = c.recv(1024)
    data = json.loads(data.decode())
    matrix_a = data.get("a")
    rows = data.get("c")
    column = data.get("d")
    result = sumAlternate(matrix_a[0][0],rows)
    print(result)
    response = json.dumps({"response":result})
    c.send(response)
c.close()