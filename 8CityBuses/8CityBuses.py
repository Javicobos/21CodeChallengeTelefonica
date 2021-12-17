lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])

#some initial thoughts: (these may not be updated after I code things)
#this could work like
# 	make a list of the cities in a case
# 	remove one city X
# 		pick city 1 and check if it can connect with cities 2-n
#		pick city 2 and check if it can connect with 3-n (we no longer have to check 1-2)
# 		do this n times for n cities, for each city i we check i-n
# 		if we ever get a missed connection, we can add X to our list	
# 	remove city Y
# 		pick city check...

# 	Another way to think about it: we want to notice elements from a grafo that are bridges between otherwise unconnected cities
# 	Watch out for triangles, B is a critical city in A-B-C but not if A and C are connected as a triangle as well
#	Maybe I could make a list of all trips from city X to 1-n and then if a city appears in ALL of them it's critical. Is that more complex or less complex?
# 		Listing all trips sounds difficult because you'd get a bazillon options if the graph has many connections maybe
# 		Like you can't just get the shortest one or the longest one, it seems intuitively less easy	

#	2nd day idea
# 	going to set up arrays for each city like [Madrid,1,1,0,0] that tell me what they are directly linked to
# 		aferwards we check each of a city's connections and add its connections as well
# 		we repeat this until there are no new connections	
	
def makeInitialMatrix(firstLineIndex, totalTrips):
	initialCityMatrix = []
	#simpleCityList = [] #some weird stuff happening here 
	for busTrip in range(totalTrips):												#we set the thing up with the cities' names
		firstCityCandidate = lines[firstLineIndex + busTrip].partition(',')[0]
		secondCityCandidate = lines[firstLineIndex + busTrip].partition(',')[2].replace('\n','')
		if firstCityCandidate not in (x[0] for x in initialCityMatrix):
			initialCityMatrix.append([firstCityCandidate])
			simpleCityList.append(firstCityCandidate)
		if secondCityCandidate not in (x[0] for x in initialCityMatrix):
			initialCityMatrix.append([secondCityCandidate])
			simpleCityList.append(secondCityCandidate)

	myTotalCities = len(initialCityMatrix)
	for city in initialCityMatrix:													#add some zeroes that will be filled up
		for unit in range(myTotalCities):
			city.append(0)
	
	for busTrip in range(totalTrips):
		firstCityCandidate = lines[firstLineIndex + busTrip].partition(',')[0]
		secondCityCandidate = lines[firstLineIndex + busTrip].partition(',')[2].replace('\n','')
		firstCityIndex = simpleCityList.index(firstCityCandidate)
		secondCityIndex = simpleCityList.index(secondCityCandidate)
		initialCityMatrix[firstCityIndex][firstCityIndex + 1] = 2
		initialCityMatrix[secondCityIndex][secondCityIndex + 1] = 2 #give each a 2 for self
		initialCityMatrix[firstCityIndex][secondCityIndex +1] = 1
		initialCityMatrix[secondCityIndex][firstCityIndex +1] = 1 #give each the 1 for the other city


	#print simpleCityList
	return initialCityMatrix

#print simpleCityList

import copy

#myTest = makeInitialMatrix(9, 16)
#myTest2 = copy.deepcopy(myTest)
#myTest2[0][0] = 'Wakanda'
#print myTest
#print myTest2
#print simpleCityList

def removeCity(cityToRemove, copyCityMatrix):
	cityRemoveIndex = simpleCityList.index(cityToRemove)
	#print cityRemoveIndex
	for index, elem in enumerate(copyCityMatrix[cityRemoveIndex][1:]):
		copyCityMatrix[cityRemoveIndex][index + 1] = 5					#5 is our special value for deleted cities, because why not
	#print copyCityMatrix[cityRemoveIndex]
	#return copyCityMatrix

#removeCity('Atoka', myTest)
#print 'city removed matrix'
#print myTest

def makeDeepConnections(removedCity, passedCityMatrix):
	removedCityIndex = simpleCityList.index(removedCity)
	copyCityMatrix = copy.deepcopy(passedCityMatrix)
	while True:
		lastCityMatrix = copy.deepcopy(copyCityMatrix)
		for index, elem in enumerate(copyCityMatrix):				#index is city index
			if index != removedCityIndex:
				for index2, connection in enumerate(copyCityMatrix[index][1:]):		#index2 will iterate thru connections
					if connection == 1:
						for index3, endConnection in enumerate(copyCityMatrix[index2][1 + index:]):
							if endConnection == 1:
								if copyCityMatrix[index][index3 + 1 + index] == 0:				#if A is connected to B, we give B's connections to A too
									copyCityMatrix[index][index3 + 1 + index] = 1
		if lastCityMatrix == copyCityMatrix:
			break
		#print 'go agane'
		#print copyCityMatrix
	return copyCityMatrix

#makeDeepConnections('Atoka', myTest) 
#print 'frst connections'
#print myTest

#makeDeepConnections('Atoka', myTest) 
#print 'second connections'
#print myTest


def CheckForConnectionButSmartNow(superIndex):
	#	removedCityIndex = simpleCityList.index(removedCity) to find removed city index
	#if superIndex == removedCityIndex:
	#	myGraphSolution[superIndex] = 5
	#else:
	#	myGraphSolution[superIndex] = 1
	myGraphSolution[superIndex] = 1
	for index2, connection in enumerate(initialCityMatrix[superIndex][1:]):		#index2 will iterate thru connections
		if connection == 1 and myGraphSolution[index2] == 0:
			#outputFile.write(passedCityMatrix[superIndex][0] + ' is connected to ' + passedCityMatrix[index2][0] + '\n')
			#outputFile.write(str(myGraphSolution) + '\n')
			#if myGraphSolution[index2] == 0:
			CheckForConnectionButSmartNow(index2)
	#outputFile.write('quitting recursion for' +  passedCityMatrix[superIndex][0])



offset = 1
for i in range(totalCases): #do I even want this loop? dunno!
	#print 'uwu ' + lines[i + offset]
	trips = int(lines[i + offset])
	#print offset
	#cityMatrix = makeInitialMatrix
	#print i + offset + 1
	#print trips
	initialCityMatrix = []
	simpleCityList = []
	initialCityMatrix = makeInitialMatrix(i + offset + 1, trips)
	offset += trips
	
	criticalCities = []

	for index5,cityToRemove in enumerate(simpleCityList):
		#print 'we are removing cities'
		#copyCityMatrix = copy.deepcopy(initialCityMatrix)
		#removeCity(cityToRemove, copyCityMatrix)
		#savedCityList = copy.copy(initialCityMatrix[index5])
		#for index10,element in enumerate(initialCityMatrix[index5][1:])
		#	initialCityMatrix[index5][1 + index10] = 
		
		
		#print 'we are making deep connections'
		#copyCityMatrix = makeDeepConnections(cityToRemove, copyCityMatrix)
		#print 'we are detecting that they are ok or not after making deep connections'
		myGraphSolution = []
		for unit in simpleCityList:
			myGraphSolution.append(0)
		#outputFile.write('I just removed ' + cityToRemove +  str(copyCityMatrix) + '\n')
		if index5 == 0:
			myGraphSolution[0] = 1
			CheckForConnectionButSmartNow(1)
		else:
			myGraphSolution[index5] = 1
			CheckForConnectionButSmartNow(0)
		#CheckForConnectionButSmartNow(startSuperIndex) #THIS TOOK SO LONG TO GET RIGHT I AM CRYING BLOOD
		if 0 in myGraphSolution:
			criticalCities.append(cityToRemove)
		print 'i have done a city'
		print index5


		#print cityToRemove
		#print myGraphSolution
		
		#for cityList in copyCityMatrix:
		#	if 0 in cityList:							#detect that the removed city was critical
				#print cityToRemove
				#print copyCityMatrix
				#print cityList
		#		criticalCities.append(cityToRemove)
		#		break





	outputFile.write('Case #' + str(i + 1) + ': ')


	#print criticalCities
	if criticalCities:
		sorted_cities = sorted(criticalCities)
		needComma = False
		for cityToWrite in sorted_cities:
			if needComma:
				outputFile.write(',')
			needComma = True
			outputFile.write(cityToWrite)
			
		#print str(sorted_cities)
	else:
		outputFile.write('-')
	
	if (i != totalCases - 1):
		outputFile.write('\n')






