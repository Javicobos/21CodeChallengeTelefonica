lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])

#firstLine = lines[1].partition('-')
#loveString = firstLine[0]
#print(loveString)
#firstLine = firstLine[2].partition('|')
#hateString = firstLine[0]
#print(hateString)

#loveDict = {'a': 2, 'e': 4, 'h': 3, 'l': 5, 'o': 1, 't': 6, 'v': 0}
#print(loveDict)
#print(loveDict['a'])


#dict constructor

#fourthLine = lines[4].partition('|')
#maybeDict = fourthLine[2]
#print(maybeDict) #this is a string

#thing = 6.0/9
#print(thing)

#import math #my bad python here does not have math.lcm so i have to do something bad
def removeDenominators(workString):	#this does not check duplicate denominators or common factors, but it should be fine as long as the words or numbers aren't supergigantic
	if '/' not in str(workString):	#i really did not want to use floats (inaccuracies are scarier than big numbers)
		return workString
	denomList = []
	for index, ele in enumerate(workString[1:][::2]):
		if '/' in ele:
			denomList.append(ele.partition('/')[2])
			#print denomList[-1]
			workString[2 * index+1] = ele.partition('/')[0]
			#print(workString[2 * index+1])
			#print ele
		else:
			denomList.append('1')
	#print denomList
	denomList = map(int, denomList)
	#print denomList
	#print workString
	#lcm = math.(denomList)
	for index1,denom in enumerate(denomList):
		if denom != 1:
			for index2, tomult in enumerate(workString[1:][::2]):
				if index2 != index1:
					workString[2 * index2 + 1] = str(int(tomult) * denom)
		denomList[index1] = 1
	#print denomList



import re			#i wanted to work without importing but this just does the thing i want
def assignToDic(assignString):
	#outString = assignString.split(',')
	assignString = assignString.replace('\n','')
	workString = re.split(',|=', assignString)
	#print(workString)
	#for i in zip(workString)
	removeDenominators(workString)
	outDict = dict(zip(workString, workString[1:])[::2]) #this came from looking up how to iterate a list over every two elements and also the dict() function
	#print(outDict)
	return outDict

#firstDic = assignToDic(firstLine[2])

def tupleToDic(tupleString):
	#tupleString = tupleString.replace('\n','')
	workString = re.split('\[| |,|\(|\)|\]|\'|\n', tupleString)
	workString = filter(None, workString)
	#print('/' in str(workString)) #tells us if there are fractions
	removeDenominators(workString)
	#print(workString)
	outDict = dict(zip(workString, workString[1:])[::2])
	#print(outDict)
	return outDict

#secondLine = lines[2].partition('|')[2]
#print(secondLine)
#secondDic = tupleToDic(secondLine)


def dicToDic(dicString):
	workString = re.split('\{| |,|\}|\'|\n|\:', dicString)
	workString = filter(None, workString)
	#print(workString)
	removeDenominators(workString)
	outDict = dict(zip(workString, workString[1:])[::2])
	#print(outDict)
	return outDict

#fourthLine = lines[4].partition('|')[2]
#thirdDic = dicToDic(fourthLine)

#need to take care of fractions
#simplify if possible, the get LCM and multiply
#

# Iterate over the string
#for i, v in enumerate(string_name):
#    print(v)

def getValueWord(word, myDict):
	value = 0
	for i,v in enumerate(word):
		value += int(myDict[v])
	return value

#valueLove = getValueWord(loveString, firstDic)
#print(valueLove)
#valueHate = getValueWord(hateString, firstDic)
#print(valueHate)

#https://docs.python.org/3/library/functions.html#divmod nvm didn't use

for i,line in enumerate(lines[1:]):
	myPartition = lines[i + 1].partition('|')
	if '=' in line:
		myGeneralDict = assignToDic(myPartition[2])
	elif '(' in line:
		myGeneralDict = tupleToDic(myPartition[2])
	elif ':' in line:
		myGeneralDict = dicToDic(myPartition[2])
	myWords = myPartition[0].partition('-')
	firstWord = myWords[0]
	secondWord = myWords[2]
	#print firstWord
	#print secondWord
	#print myGeneralDict
	firstWordValue = getValueWord(firstWord, myGeneralDict)
	secondWordValue = getValueWord(secondWord, myGeneralDict)
	outputFile.write('Case #' + str(i + 1) + ': ')
	if firstWordValue > secondWordValue:
		outputFile.write(firstWord)
	elif firstWordValue < secondWordValue:
		outputFile.write(secondWord)
	else:
		outputFile.write('-')
	if (i != totalCases - 1):
		outputFile.write('\n')
