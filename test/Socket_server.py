#! /usr/bin/python3.5

import socket
s=socket.socket()
host=socket.gethostname()
print(host)
port=50007
#host='10.0.0.245'
s.bind((host, port))
s.listen(5)
while True:
    c,addr=s.accept()
    print ('Got connection from', addr)
    c.send('Thank you for connectioning')
    c.close()

