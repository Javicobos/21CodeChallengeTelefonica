
lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])

num1 = 0
num2 = 0
numSum = 0
for index, item in enumerate(lines[1:]):
	num1 = int(item[0])
	num2 = int(item[2])
	numSum = num1 + num2 + 1
	outputFile.write('Case #' + str(index + 1) + ': ')
	if (numSum != 13):
		outputFile.write(str(numSum))
	else:
		outputFile.write('-')
	if (index + 1 != totalCases):
		outputFile.write('\n')
	
outputFile.close()
