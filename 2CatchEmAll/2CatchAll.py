lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])
#print('totalcases is ' + str(totalCases))

#poketoFind = int(lines[1])
#print('poketofind is '  +str(poketoFind))

#case1Description = lines[1].split()
#print(case1Description)
#case1Pokes = int(case1Description[0])
#case1Rows = int(case1Description[1])
#case1Columns = int(case1Description[2])
#print(case1Pokes)
#print(case1Rows)
#print(case1Columns)

#lineToJoin = lines[4]
#print(lineToJoin)
#lineToJoin = lineToJoin.replace(' ','')
#lineToJoin = lineToJoin.replace('\n','')
#print(lineToJoin) 

#caseALADescription = lines[18].split()
#print(caseALADescription)
#caseALAPokes = int(caseALADescription[0])
#caseALARows = int(caseALADescription[1])
#caseALAColumns = int(caseALADescription[2])

#stringALA = ""
#for i in range(caseALARows):
#	tempStr = lines[20 + i]
#	tempStr = tempStr.replace(' ','')
#	tempStr = tempStr.replace('\n','')
#	stringALA += tempStr
#print(stringALA)

caseGENERALdesc = ""
offset = 1
for i in range(totalCases):
	caseGENERALdesc = lines[offset].split()
	caseGENERALPokes = int(caseGENERALdesc[0])
	caseGENERALRows = int(caseGENERALdesc[1])
	caseGENERALColumns = int(caseGENERALdesc[2])
	stringGENERAL = ""
	for j in range(caseGENERALRows): #we write the "map" as a single string
		tempStr = lines[offset + caseGENERALPokes + 1 + j]
		tempStr = tempStr.replace(' ','')
		tempStr = tempStr.replace('\n','')
		stringGENERAL += tempStr
	listPokes = []
	for k in range(caseGENERALPokes):
		listPokes.append(lines[offset + k + 1])
		listPokes[k]  = listPokes[k].replace('\n','')
	#print(listPokes)
	listReversePokes = []
	for l in listPokes:
		listReversePokes.append(l[::-1])
	#print(listReversePokes)
	#print('Im on step ' + str(i) + ' and my original stringGENERAL is: ' + stringGENERAL)
	foundPokes = 0
	while (foundPokes != caseGENERALPokes):
		pokeIndex = 0
		while (pokeIndex < caseGENERALPokes - foundPokes):
			if (listPokes[pokeIndex] in stringGENERAL):
				stringGENERAL = stringGENERAL.replace(listPokes[pokeIndex], '')
				foundPokes += 1
				listPokes.pop(pokeIndex)
				listReversePokes.pop(pokeIndex)
			elif (listReversePokes[pokeIndex] in stringGENERAL):
				stringGENERAL = stringGENERAL.replace(listReversePokes[pokeIndex], '')
				foundPokes += 1
				listPokes.pop(pokeIndex)
				listReversePokes.pop(pokeIndex)
			else:
				pokeIndex += 1

		#for m, item in enumerate(listPokes):			this was less cool because it searched for things that had been found already
		#	if (item in stringGENERAL):
		#		#print('found ' + item + ' in ' + stringGENERAL)
		#		stringGENERAL = stringGENERAL.replace(item, '')
		#		#print('stringGeneral is now: ' + stringGENERAL)
		#		foundPokes += 1
		#	elif (listReversePokes[m] in stringGENERAL):
		#		stringGENERAL = stringGENERAL.replace(listReversePokes[m], '')
		#		foundPokes += 1
	#print('Im on step ' + str(i) + ' and my stringGENERAL is: ' + stringGENERAL)

	#	for m in range(caseGENERALPokes):
	#		if (lines[offset + m] in stringGENERAL)
	#			stringGENERAL.replace(lines[offset + m], '')
	#			foundPokes + = 1
	outputFile.write('Case #' + str(i + 1) + ': ' + stringGENERAL)
	if (i != totalCases - 1):
		outputFile.write('\n')
	offset += caseGENERALPokes + caseGENERALRows + 1

outputFile.close()