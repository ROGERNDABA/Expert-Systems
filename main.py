#!/usr/bin/env python3
import json
import sys
import os.path
import re
import handler
from pprint import pprint


FactHandler = handler.FactHandler()


def replace_all(text, dic):
	for i, j in dic.items():
		text = text.replace(i, str(j))
		text = text.replace("Falsealse", "False")
		text = text.replace("Truerue", "True")
	return text


def split(word):
	word = word.replace(" ", "")
	return [char for char in word]


if len(sys.argv) == 2:
	if os.path.exists(sys.argv[1]) == True:
		f = open(sys.argv[1], "r")
		validFileLines = []
		validFacts = {}
		for line in f:
			if line[0] == "#":
				continue
			x = line.split()
			l = [x.index(i) for i in x if "#" in i]
			validFileLines.append(x[: l[0]]) if l else validFileLines.append(x)
		validFacts = FactHandler.validateAvailableOptions(validFileLines)
		validFileLines = [" ".join(listItem) for listItem in validFileLines if listItem]

		print(validFileLines)
		validFileLines = validFileLines[:-2]
		print(json.dumps(validFacts, indent=2))
		lexer = ""
		restart = True

		operands = {"+": "and", "!": "not ", "|": "or", "^": "!="}
		while restart:
			for part in validFileLines:
				part1 = replace_all(replace_all(part, validFacts), operands)
				part1 = re.split("\W=>\W|\W<=>\W", part1)
				part = re.split("\W=>\W|\W<=>\W", part)
				if re.match(r"[A-Z]$", part[1]):
					if eval(part1[1]) == False and eval(part1[0]) == True:
						validFacts[part[1]] = True
				else:
					print(part)
				restart = False
				# elif re.match(r"[A-Z]\W\+\W[A-Z]", part[1]):
				# print(eval(part1[0]))
			print(json.dumps(validFacts, indent=2))
		print(lexer)
		validFileLines = [
			re.findall(r"\([^()]*\)|<?=>|[-+/*|^]|\w+", listItem)
			for listItem in validFileLines[:-2]
		]

		# print()
		# print(json.dumps(validFileLines, indent=2))
		############# printing ##################

		# for vals in col1:
		# 	row_format = '{:<6}' * (len(vals))
		# 	print (row_format.format(*vals))

		############# printing end ##############

	else:
		print("\033[91mno such file or directory\033[0m")
else:
	print("\033[91minvalid number of arguments\033[0m")

# reserved for next attempt
# ^[A-Z]*(=>|<=>)[A-Z]*$
