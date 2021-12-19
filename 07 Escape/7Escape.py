import os

#stream = os.popen('nc codechallenge-daemons.0x14.net 4321')
#output = stream.read()
#print	output

outputFile = open('testOutput.txt', 'w')

import subprocess

process = subprocess.Popen(['nc', 'codechallenge-daemons.0x14.net', '4321'], stdin=subprocess.PIPE ,stdout=subprocess.PIPE, universal_newlines=True)

bigMatrixMoves = []

solutionString = '(0, 0)'

allSolutionsMatrix = []

while True:
	output = process.stdout.readline()
	print(output.strip())
	if 'beginning' in output:
		print('AAAAAAAAAAAAAAAAA')
		#process = process.communicate(input='west')[0]
		#process.stdin.write('west')
		#print 'we went west'
		#output = process.stdout.readline()
		#print(output.strip())
		process.stdin.write('west')
	# Do something else

	if 'Great movement.' in output:
		myPosition = output.replace('\n','').partition(':')[2].strip()
		print myPosition
		if myPosition not in (x[0] for x in bigMatrixMoves):
			myPositionAsList = [myPosition]
			bigMatrixMoves.append(myPositionAsList)
			#print bigMatrixMoves
		if myPosition not in solutionString:
			solutionString += ', ' + myPosition
		else:
			solutionString = solutionString.partition(myPosition)[0]
			solutionString += myPosition
		print solutionString
		process.stdin.write('is exit?')

	if 'No. Sorry, traveller' in output:
		process.stdin.write('look')
	if 'Congratulations, you found the exit door' in output:
		#print 'SOLUTION FOUND'
		#outputFile.write(solutionString)
		#outputFile.write('\n')
		#print len(solutionString)
		allSolutionsMatrix.append(solutionString)
		process.stdin.write('look')


	if 'You could do these movements' in output:
		givenMoves = output.replace('\n','').partition(':')[2].split()
		for index, elem in enumerate(bigMatrixMoves):
			if myPosition in bigMatrixMoves[index]:
				myPositionIndex = index
		#print myPositionIndex
		if len(bigMatrixMoves[myPositionIndex]) == 1:
			bigMatrixMoves[myPositionIndex].extend(givenMoves) #-1 will not work for backtracking
		#print bigMatrixMoves
		if 'west' in bigMatrixMoves[myPositionIndex]:
			bigMatrixMoves[myPositionIndex][bigMatrixMoves[myPositionIndex].index('west')] = '0'
			process.stdin.write('west')
		elif 'north' in bigMatrixMoves[myPositionIndex]:
			bigMatrixMoves[myPositionIndex][bigMatrixMoves[myPositionIndex].index('north')] = '0'
			process.stdin.write('north')
		elif 'east' in bigMatrixMoves[myPositionIndex]:
			bigMatrixMoves[myPositionIndex][bigMatrixMoves[myPositionIndex].index('east')] = '0'
			process.stdin.write('east')
		elif 'south' in bigMatrixMoves[myPositionIndex]:
			bigMatrixMoves[myPositionIndex][bigMatrixMoves[myPositionIndex].index('south')] = '0'
			process.stdin.write('south')
		else:
			print 'maze fully transversed!'
			optimalSolution = min(allSolutionsMatrix, key=len)
			outputFile.write(optimalSolution)
			print optimalSolution
			break

	#Yes. Congratulations, you found the exit door

	return_code = process.poll()
	if return_code is not None:
		print('RETURN CODE', return_code)
		# Process has finished, read rest of the output 
		for output in process.stdout.readlines():
			print(output.strip())
		break

