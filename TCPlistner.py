#! /usr/bin/python3
import socket

TCP_IP = "127.0.0.1" # declare our ip and port to listen on
TCP_PORT = 6996
BUFFER_SIZE = 1024 # recv bytes

with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s: # AF_INET -> address (IPv4), SOCK_STREAM -> socket type (TCP)
    s.bind((TCP_IP, TCP_PORT)) # bind the socket to the address and port
    s.listen()
    print(f"Server listening on {TCP_IP}:{TCP_PORT}...")

    # This loop lets the server accept new clients until ctrl+c
    while True:
        conn, addr = s.accept()
        with conn:
            print(f"Connection from: {addr}")
            while True:
                data = conn.recv(BUFFER_SIZE)
                if not data:
                    break  # Client closed the connection
                print(f"Received: {data.decode()}")
                conn.send(data) # echo
            print(f"Connection with {addr} closed.")
