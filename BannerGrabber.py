#! /usr/bin/python3
import socket

Ports = [21, 22, 25, 80, 443, 3306] # Modify ports here
IP = "127.0.0.1"                    # Change IP you want to scan
TIMEOUT = 2                         # n seconds for timing out

print(f"Scanning {IP}")

for Port in Ports:
    with socket.socket(socket.AF_INET, socket.SOCK_STREAM) as s:
        s.settimeout(TIMEOUT)
        
        try:
            s.connect((IP, Port))
            answer = s.recv(1024)
            print(f"[+] Port {Port} discovered")
            print(answer.decode())

        except ConnectionRefusedError:
            print(f"\nConnection failed on port {Port}")

print("\nScan complete")
