#! /usr/bin/python3
import socket

TCP_IP = "127.0.0.1" # declare our ip and port to listen on
TCP_PORT = 6996
BUFFER_SIZE = 1000 # recv bytes

s = socket.socket(socket.AF_INET, socket.SOCK_STREAM) # AF_INET -> address (IPv4), SOCK_STREAM -> socket type (TCP)
s.bind((TCP_IP, TCP_PORT)) # bind the socket to the address and port
s.listen(1)
print(f"Server is listening on {TCP_IP}:{TCP_PORT}...")

conn, addr = s.accept() # waiting until a client connects
print(f"Connection address: {addr}")

while True: # looping until the connection is closed
	data = conn.recv(BUFFER_SIZE)
	if not data:
		break
	print(f"Received data: {data.decode()}") #.decode() converts a bytes object into a string
	conn.send(data)

conn.close()
print("Connection closed")
