lines = []
with open('testInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('testOutput.txt', 'w')

totalCases = int(lines[0])

firstLine = lines[1].partition('-')
loveString = firstLine[0]
#print(loveString)
firstLine = firstLine[2].partition('|')
hateString = firstLine[0]
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

import re			#i wanted to work without importing but this just does the thing i want
def assignToDic(assignString):
	#outString = assignString.split(',')
	assignString = assignString.replace('\n','')
	workString = re.split(',|=', assignString)
	#print(workString)
	outDict = {}
	#for i in zip(workString)
	outDict = dict(zip(workString, workString[1:])[::2]) #this came from looking up how to iterate a list over every two elements and also the dict() function
	print(outDict)
	return outDict

firstDic = assignToDic(firstLine[2])

def tupleToDic(tupleString):
	#tupleString = tupleString.replace('\n','')
	workString = re.split('\[| |,|\(|\)|\]|\'|\n', tupleString)
	workString = filter(None, workString)
	#print(workString)
	outDict = dict(zip(workString, workString[1:])[::2])
	print(outDict)
	return outDict

secondLine = lines[2].partition('|')[2]
#print(secondLine)
secondDic = tupleToDic(secondLine)


def dicToDic(dicString):
	workString = re.split('\{| |,|\}|\'|\n|\:', dicString)
	workString = filter(None, workString)
	outDict = dict(zip(workString, workString[1:])[::2])
	print(outDict)
	return outDict

fourthLine = lines[4].partition('|')[2]
thirdDic = dicToDic(fourthLine)

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

valueLove = getValueWord(loveString, firstDic)
print(valueLove)
valueHate = getValueWord(hateString, firstDic)
print(valueHate)