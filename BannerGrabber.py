#! /usr/bin/python3
import socket

try:
    with socket.socket() as s:  # set s as socket
        s.connect(("127.0.0.1", 22))
        answer = s.recv(1024)
        print(answer.decode())
except ConnectionRefusedError:  # 'except' catches the error if the server is not running
    print("Connection failed")
