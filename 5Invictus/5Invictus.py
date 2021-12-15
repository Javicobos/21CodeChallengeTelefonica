# -*- coding: utf-8 -*-

lines = []
with open('Invictus.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('testOutput.txt', 'w')

import re

#codedLetters = ''

for i,line in enumerate(lines):
	numbersOut = []
	for index,v in enumerate(line):
		#outputFile.write(v)
		if ord(v) > 127:
			#print v
			#print ord(v)
			#print chr(ord(v) - 127)
			if ord(v) != 243:
				if ord(v) != 160:
					numbersOut.append(ord(v))
			#outputFile.write('Ñ')
	#outputFile.write(line)
	#for e in elements:
	#if (re.sub('[ -~]', '', line)) != "":
	#	outputFile.write(line)
	for index2,elem in enumerate(numbersOut[::2]):
		numbersOut[index2 * 2] = elem - 129
	if numbersOut:
		#print numbersOut
		diffs = []
		for index3,num in enumerate(numbersOut[3:][::2]):
			myDiff = num - numbersOut[2*index3 + 3 -2]
			diffs.append(myDiff)
			#print num
			#print numbersOut[2*index3 + 3 - 2]
		#print diffs

	#50-60 did some Ms
	#for crack in range(100,110):
	codedLetters = ''
	for index2,num in enumerate(numbersOut[1:][::2]):
		if numbersOut[2* index2] == 0:
			codedLetters += chr(num - 110) #used the diffs between chars 4 apart
		else:
			codedLetters += chr(num - 46) #used the S in nelson to crack this
	#print codedLetters
	outputFile.write(codedLetters)
	#codedLetters += '-------'

#print codedLetters


# 77 65 78 68 69 76 65 
# M A N D E L A
# diffs are:
#  -12 +13 -10 +1 +7 -11  