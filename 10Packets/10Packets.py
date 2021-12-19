lines = []
with open('pcap_console_output.txt', 'r') as f:
	lines = f.readlines()
outputFile = open('testOutput.txt', 'w')
outPNG = open('testOutPNG.png', 'w')

fullarray = []
for index,line in enumerate(lines[::3]):
	ipNumber = int(line.partition('31.')[2].partition(' ')[0])
	idNumber = int(line.partition('id ')[2].partition(',')[0])
	seqNumber = int(line.partition('seq ')[2].partition(',')[0])

	packetContent = lines[3 * index + 2].partition('0800 ')[2].replace('\n','').replace('......','',1)
	#print str([ipNumber, idNumber, seqNumber]) + ' \t' + packetContent #What a mess, you will need to reorder everything to get the price
	fullarray.append([seqNumber, idNumber, ipNumber, packetContent])



	#outputFile.write([idNumber, ipNumber, seqNumber]) + ' \t' + packetContent)

fullarray.sort()		#sorting by idnumber sorts the middle alphabetically
for i in fullarray:
	outputFile.write( i[3].partition('      ')[0].split()[-1]  + '\t')
	outputFile.write(i[3][-1])
	outputFile.write('\n')
	specialInt = int( i[3].partition('      ')[0].split()[-1],  16)
	print specialInt
	outPNG.write(chr(specialInt))
	
for i in fullarray:	#sorting by seq gives us PNG stuff on the right
	#print i
	for j in i:
		outputFile.write(str(j) + '\t')
	outputFile.write('\n')

#http://www.libpng.org/pub/png/spec/1.2/PNG-Chunks.html
