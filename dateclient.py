import socket
import os
from ftplib import FTP
from datetime import date
import calendar

class Client:
    def __init__(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.connect_to_server()

    def connect_to_server(self):
        self.target_ip = '127.0.0.1'
        self.target_port = 8080

        self.s.connect((self.target_ip,int(self.target_port)))

        self.main()

    def reconnect(self):
        self.s = socket.socket(socket.AF_INET,socket.SOCK_STREAM)
        self.s.connect((self.target_ip,int(self.target_port)))

    def main(self):
        while 1:
            file_name = 'input.txt'
            self.s.send(file_name)

            confirmation = self.s.recv(1024)
            if confirmation.decode() == "file-doesn't-exist":
                print("File doesn't exist on server.")

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

            else:        
                write_name = 'from_server '+file_name
                if os.path.exists(write_name): os.remove(write_name)

                with open(write_name,'w+') as file:
                    while 1:
                        data = self.s.recv(1024)

                        if not data:
                            break

                        file.write(data)
                        ManavMonth=(int)(data[0]+data[1])
                        print(type(ManavMonth))
                        print("The number of month: ")
                        print(ManavMonth)
                        Year= 2021
                        A=calendar.TextCalendar(calendar.SUNDAY)
                        for b in range(1,13):
                            if b!=ManavMonth:
                                continue
                            for k in A.itermonthdays(Year,b):
                                if k!=0:
                                    day=date(Year,b,k)
                                    if day.weekday()==6:
                                        print("%s,%d-%d-%d" % (calendar.day_name[6] ,k,b,Year))


                print(file_name,'successfully downloaded.')

                self.s.shutdown(socket.SHUT_RDWR)
                self.s.close()
                self.reconnect()

client = Client()
