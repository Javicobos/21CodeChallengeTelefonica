lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])





#		A 				0
#		A# Bb			1
#		B Cb			2
#		B# C			3
#		C# Db			4
#		D				5
#		D# Eb			6
#		E Fb			7
#		E# F			8
#		F# Gb			9
#		G 				10
#		G# Ab			11
#		A 				0 (12)

notesMatrix = [['A'],['A#','Bb'],['B','Cb'],['B#','C'],['C#','Db'],['D'],['D#','Eb'],['E','Fb'],['E#','F'],['F#','Gb'],['G'], ['G#', 'Ab']]
#for i in notesMatrix:
#	print i


def getValueTone(toneChar):
	if toneChar == 'T':
		return 2
	else:
		return 1


for i,line in enumerate(lines[1:][::2]):
	startNote = line.replace('\n', '')
	#print startNote
	#print lines[2*i + 2].replace('\n', '') #this is the line with the tones
	for index,elem in enumerate(notesMatrix):
		for index2, elem2 in enumerate(elem):
			if startNote == elem2:
				#print(startNote)
				noteValue = index
				#print(noteValue)
				break
	outputNotes = startNote
	for index3 in range(6):
		noteValue += getValueTone(lines[2*i + 2][index3])
		noteValue = noteValue % 12
		if notesMatrix[noteValue][0][0] not in outputNotes:
			outputNotes += notesMatrix[noteValue][0]
		else:
			#print notesMatrix[noteValue]
			outputNotes += notesMatrix[noteValue][1]
	outputNotes += startNote
	outputFile.write('Case #' + str(i + 1) + ': ')
	outputFile.write(outputNotes)
	if (i != totalCases - 1):
		outputFile.write('\n')