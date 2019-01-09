#!/usr/bin/env python3
from array import *
import sys
import os.path

class Handler:
	def __init__(self):
		self.name = 'roger'
		self.age = 20

	def Start(self, ar):
		print (ar + ' hello ' + self.name)


if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]) == True:
		f = open(sys.argv[1], "r")
		col = []
		i = 0
		for line in f:
			if line[0] == '#':
				continue
			x = line.split()
			if "#" in x:
				x2 = x[:x.index("#")]
				col.append(x2)
		for vals in col:
			print(vals)
	else:
		print('\033[91mno such file\033[0m')
else:
	print('\033[91minvalid number of arguments\033[0m')

#
human = Handler()
# human.Start('you')
