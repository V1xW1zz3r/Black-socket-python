#! /usr/bin/python3

import socket
s = socket.socket() # we set "s" as our socket.socket()
s.connect(("127.0.0.1", 22)) # feel free to change ip and port

answer = s.recv(1024) # receive and read the 1024 bytes of data from socket

print(answer)
s.close() # close the connection
print("Connection closed")
