#!/usr/bin/python3

import sys  
import socket  
import argparse
from threading import Thread  

# global vars 
parser = argparse.ArgumentParser()
parser.add_argument("-ip", "--ipaddr", help="Prints IP address only", action="store_true")
args = parser.parse_args()


def GIP(domain):
	IP = socket.gethostbyname(domain)
	if args.ipaddr:
		print(IP)
	else:
		print(domain+","+IP)

def GetIP(domain):
	try:
		GIP(domain)
	except:
		try:
			GIP(domain)
		except:
			try:
				GIP(domain)	
			except:
				pass
	finally:
		pass
	
if __name__ == "__main__":  
	while True:
		try:
			base_domain = input()
			domain = str(base_domain.strip('\n'))
			t = Thread(target=GetIP, args=(domain,))  
			child = t.start()
		except EOFError:
			t.join()
			sys.exit()
