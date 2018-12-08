#!/usr/bin/env python3

import sys
import os.path

class Handler:
	def __init__(self):
		self.name = 'roger'
		self.age = 20

	def Start(arg, ar):
		print (ar + ' hello ' + arg.name)






if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]) == True:
		f = open(sys.argv[1], "r")
		for line in f:
			if line[0] == '#':
				continue
			else:
				print(line, end='')
	else:
		print('\033[91mno such file\033[0m')
else:
	print('\033[91minvalid number of arguments\033[0m')

#
human = Handler()
# human.Start('you')
