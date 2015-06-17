#!/usr/bin/env python

import threading
import time

class AsynchWrite(threading.Thread):
	"""docstring for AsynchWrite"""
	def __init__(self, text, outfilename):
		threading.Thread.__init__(self)
		self.text = text
		self.outfilename = outfilename

	def run(self):
		f=open(self.outfilename, "a")
		f.write(self.text + "\n")
		f.close()
		print "Background writing of file completed"


def Main():
	message = raw_input("Enter the message to be written: ")
	asyncWriteobject= AsynchWrite(message, "outputLearnthreading2.txt")
	asyncWriteobject.start()
	print "The Program is running while the file is written in another thread"
	print "Test: " + str(100+100)
	asyncWriteobject.join()
	print "The main program waited until the main thread was completed"

if __name__ == '__main__':
		Main()	
