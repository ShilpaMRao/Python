# World's simplest Web Browser

import socket

mysocket = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
mysocket.connect(('data.pr4e.org',80)) # connect to host , on port

cmd = 'GET http://http://data.pr4e.org/intro-short.txt HTTP/1.0\r\n\r\n'.encode()

mysocket.send(cmd)

while True:
    data = mysocket.recv(512)
    if len(data) < 1:
        break
    print(data.decode(),end='')

mysocket.close()


