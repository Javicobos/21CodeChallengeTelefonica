lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()
outputFile = open('submitOutput.txt', 'w')
totalCases = int(lines[0])
totalSprites = int(lines[1])

#
myStart = 3
#myWidth = int(lines[myStart - 1].partition(' ')[0])
#myLength = int(lines[myStart - 1].partition(' ')[2].replace('\n',''))
#print myWidth
#print myLength
#

def make_sprite_matrix(start, myWidth, myLength):
	#myWidth = int(lines[start - 1].partition(' ')[0])
	#myLength = int(lines[start - 1].partition(' ')[2].replace('\n',''))
	mySpriteMatrix = []
	for spriteLine in range(myLength):
		myLineMatrix = []
		for spriteChar in range(myWidth):
			myLineMatrix.append(int(lines[start + spriteLine][spriteChar]))
		mySpriteMatrix.append(myLineMatrix)
		#print lines[start + spriteLine].replace('\n','')
	#print mySpriteMatrix
	return mySpriteMatrix

spriteInfoMatrix = []
megaSpriteMatrix = []
spriteInfoOffset = 2
for spriteInfoLine in range(totalSprites):
	myWidth = int(lines[spriteInfoOffset].partition(' ')[0])
	myLength = int(lines[spriteInfoOffset].partition(' ')[2].replace('\n',''))
	mySpriteSizeList = [myWidth, myLength]
	spriteInfoMatrix.append(mySpriteSizeList)
	megaSpriteMatrix.append(make_sprite_matrix(spriteInfoOffset + 1, myWidth, myLength))
	spriteInfoOffset += myLength + 1

#print spriteInfoMatrix
#print megaSpriteMatrix
#print spriteInfoOffset
#print lines[spriteInfoOffset] #this is the first map


#make_sprite_matrix(3, spriteInfoMatrix[0][0], spriteInfoMatrix[0][1])

def where_overlap(s1, s1x, s1y, s2, s2x, s2y):
	s1Width = spriteInfoMatrix[s1][0]
	s1Length = spriteInfoMatrix[s1][1]
	s2Width = spriteInfoMatrix[s2][0]
	s2Length = spriteInfoMatrix[s2][1]
	if (s1x + s1Width < s2x) or (s1y + s1Length < s2y) or (s2x + s2Width < s1x) or (s2y + s2Length < s1y):
		return #no intersection
	if s1x <= s2x:	#sprite 2 has some left part in sprite 1
		s1xOffset = s2x - s1x
		s2xOffset = 0 
		xToCompare = min(s1Width - s1xOffset , s2Width)
	else:
		s2xOffset = s1x - s2x
		s1xOffset = 0
		xToCompare = min(s2Width - s2xOffset , s1Width)

	if s1y <= s2y:
		s1yOffset = s2y - s1y
		s2yOffset = 0 
		yToCompare = min(s1Length - s1yOffset , s2Length)
		#print 'here'
	else:
		s2yOffset = s1y - s2y
		s1yOffset = 0
		yToCompare = min(s2Length - s2yOffset , s1Length)
		#print 'coords in overlapfunction are: ' + str([s2Length, s2yOffset, s1y, s2y])
		#print 'here22222'

	return [s1xOffset, s2xOffset, xToCompare, s1yOffset, s2yOffset, yToCompare]
	#print s1xOffset
	#print s2xOffset
	#print xToCompare
	#print s1yOffset
	#print s2yOffset
	#print yToCompare


#print where_overlap(0, 0, 0, 1, 2, 2)
mapOffset = spriteInfoOffset
for i in range(totalCases):
	print 'case is: ' + str(i) + ' at line ' + str(mapOffset)
	spritesInTest = int(lines[mapOffset].replace('\n',''))
	collisionsFound = 0
	spritesInTestMatrix = []
	for spritePlaced in range(spritesInTest):
		miniSpriteSplit = lines[mapOffset + spritePlaced + 1].split()
		spritesInTestMatrix.append( [int(miniSpriteSplit[0]), int(miniSpriteSplit[1]), 
			int(miniSpriteSplit[2].replace('\n', ''))])
	#print spritesInTestMatrix
	for spriteChecking in range(spritesInTest):
		if spriteChecking % 10 == 0:
			print 'checking sprite ' + str(spriteChecking) + ' out of ' + str(spritesInTest)
		for spriteChecking2 in range(spritesInTest - spriteChecking - 1):
			myOverlap = where_overlap(spritesInTestMatrix[spriteChecking][0], 
				spritesInTestMatrix[spriteChecking][1], spritesInTestMatrix[spriteChecking][2],
				spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][0],
				spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][1],
				spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][2])
			if myOverlap:
				#print myOverlap
				singleCollisionFound = False
				for indexY, y in enumerate(megaSpriteMatrix[spritesInTestMatrix[spriteChecking][0]][myOverlap[3]:]): #[myOverlap[3]:] is s1yOverlap
					if indexY == myOverlap[5]:
						break
					#print y
					#print indexY
					for indexX, x in enumerate(y[myOverlap[0]:]):														#[myOverlap[0]:] is s1xOverlap
						if indexX == myOverlap[2]: #xtocompare 
							break
						if x == 1:
							#print 'case is ' + str(i)
							#print 'second matrix is' + str(megaSpriteMatrix[spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][0]])
							#print 'im looking at' + str(megaSpriteMatrix[spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][0]][indexY + myOverlap[4]])
							#print len(megaSpriteMatrix[spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][0]])
							#print 'second coords are' + str([indexY + myOverlap[4], indexX + myOverlap[1]])
							if megaSpriteMatrix[spritesInTestMatrix[spriteChecking + spriteChecking2 + 1][0]][indexY + myOverlap[4]][indexX + myOverlap[1]] == 1:
								#print 'collision found for case' + str(i) + ' at '  + str([indexY, indexX])
								singleCollisionFound = True
								break
					if singleCollisionFound:
						collisionsFound += 1
						break
		



	outputFile.write('Case #' + str(i + 1) + ': ' + str(collisionsFound))
	if (i != totalCases - 1):
		outputFile.write('\n')
	mapOffset += spritesInTest + 1


#overlapInfo = where_overlap(0, 0, 0, 1, 2, 2)
#if overlapInfo:
	