#!/usr/bin/env python3
import sys
import os.path
import re

class Handler:

	# In other languages it's called a constructor

	def __init__(self):
		self.init = 1

	# Take all available options from the input file
	
	# Also sets options as keys with their corresponding -
	# facts (True|False) as values in a dictionary then
	# returns the dictionary

	def getOptions(self, col1):
		options = 'ABCDEFGHIJKLMNOPQRSTUVWXYZ'
		listString = ''.join(list(map(''.join, col1)))
		optDict = {}
		for x in options:
			if x in listString:
				optDict[x] = False
		return (optDict)

	#  Goes though the dictionary and change all the given options' -
	# facts from False to true then return the updated fact dictionary

	def validateAvailableOptins(self, col1):
		col2 = list(map(''.join, col1))
		factDict = self.getOptions(col1)
		r = re.compile(r'\?[A-Z]*$')
		newlist = list(filter(r.match, col2))
		if len(newlist) == 1:
			for key in newlist[0]:
				if key in factDict:
					factDict[key] = True
		return (factDict)
		
	

handler = Handler()

if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]) == True:
		f = open(sys.argv[1], "r")
		col1 = []
		for line in f:
			if line[0] == '#':
				continue
			x = line.split()
			l = [x.index(i) for i in x if '#' in i]
			col1.append(x[:l[0]]) if l else col1.append(x)
		print (handler.validateAvailableOptins(col1))


		############# printing ##################

		# for vals in col1:
		# 	row_format = '{:<6}' * (len(vals))
		# 	print (row_format.format(*vals))

		############# printing end ##############


	else:
		print('\033[91mno such file or directory\033[0m')
else:
	print('\033[91minvalid number of arguments\033[0m')

#
