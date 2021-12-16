lines = []
with open('testInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('testOutput.txt', 'w')

totalCases = int(lines[0])

for i in range(totalCases): #do I even want this loop? dunno!





	outputFile.write('Case #' + str(i + 1) + ': ' + 'WIP')
	if (i != totalCases - 1):
		outputFile.write('\n')


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

