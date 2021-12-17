lines = []
with open('testInput.txt', 'r') as f:
	lines = f.readlines()
outputFile = open('testOutput.txt', 'w')
totalCases = int(lines[0])
totalSprites = int(lines[1])