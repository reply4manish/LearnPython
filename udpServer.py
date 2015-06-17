#!/usr/bin/env python
import socket
def Main():
	host = '127.0.0.1'
	port = 5000

	s = socket.socket(socket.AF_INET, socket.SOCK_DGRAM)
	s.bind((host,port))

	print "Server started............"
	while True:
		data, addr = s.recvfrom(1024)
		print "Message from: " + str(addr)
		print "Data from user/clinet :" + str(data)
		data = str(data).upper()
		print "Sendin data: " + str(data)
		s.sendto(data, addr)
	s.close()
if __name__ == '__main__':
			Main()		