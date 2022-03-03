#!/bin/python

import sys
import socket
from datetime import datetime

#Defining the target
if len(sys.argv) == 2:
	target = socket.gethostbyname(sys.argv[1]) #Translating hostname to IPv4
else:
	print("Invalid amount of arguments.")
	print("syntax: python3 portscan.py <ip>")
	
#Banner message
print("-" * 50)
print("Scanning Target "+target)
print("Time started : "+str(datetime.now()))
print("-" * 50)

try:
	for port in range(0,65535):
		s = socket.socket(socket.AF_INET, socket.SOCK_STREAM)
		socket.setdefaulttimeout(1)
		result = s.connect_ex((target,port))
		if result == 0:
			print("port {} is open".format(port))
		s.close()

except keyboardInterrupt:
	print("\nExiting program.")
	sys.exit()

except socket.gaierror:
	print("Hostname could not be resolved.")
	sys.exit()
	
except socket.error:
	print("Could not connect to server.")
	sys.exit()
	