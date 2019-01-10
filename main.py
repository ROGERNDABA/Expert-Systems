#!/usr/bin/env python3
import sys
import os.path
import re

# class Handler:
# 	def __init__(self):
# 		self.name = 'roger'
# 		self.age = 20

# 	def Start(self, ar):
# 		print (ar + ' hello ' + self.name)


if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]) == True:
		f = open(sys.argv[1], "r")
		col = []
		for line in f:
			if line[0] == '#':
				continue
			x = line.split()
			l = [x.index(i) for i in x if '#' in i]
			col.append(x[:l[0]]) if l else col.append(x)

		############# printing ##################
		
		for vals in col:
			row_format = '{:<6}' * (len(vals))
			print (row_format.format(*vals))

		############# printing end ##############
	else:
		print('\033[91mno such file\033[0m')
else:
	print('\033[91minvalid number of arguments\033[0m')

#
# human = Handler()
# human.Start('you')
