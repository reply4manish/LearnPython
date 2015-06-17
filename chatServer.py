#!/usr/bin/env python

import time
import socket

host='127.0.0.1'
port=5000

clients = []

s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
s.bind((host,port))
s.setblocking(0)

quiting=False
print 'server started...'

while not quiting:
	try :

		data, addr = s.recvfrom(1024)
		if 'quit' in str(data):
			quiting = True
		if addr not in clients :
			clients.append(addr)

		print time.ctime(time.time()) + str(addr) + ": :" + str(data)
	    
		for client in clients :
			s.sendto(data, client)

	except :
		pass
s.close()		