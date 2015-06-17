#!/usr/bin/env python

import socket


def Main():

	host='127.0.0.1'
	port=5000

	s = socket.socket()
	s.bind((host,port))
	
	s.listen(1)
	c, address = s.accept()
	print "Connection from client: " + str(address) + "accepted"

	while True:
		data = c.recv(1024)
		if not data:
			break
		print "Data from client is : " + str(data)
		data=str(data).upper() + " Thank you"
		print "Sendin :" + data
		c.send(data)
	c.close()
	

if __name__ == '__main__':
				Main()			



