# -*- coding: utf-8 -*-
lines = []
with open('submitInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('submitOutput.txt', 'w')

totalCases = int(lines[0])


languageCodes = ['CA', 'CZ', 'DE', 'DK', 'EN', 'ES', 'FI', 'FR', 'IS', 'GR',
	'HU', 'IT', 'NL', 'VI', 'PL', 'RO', 'RU', 'SE', 'SI', 'SK']

daysOfWeek = [
	['dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte', 'diumenge'],						#CA, Catalan
	['pondělí', 'úterý', 'středa', 'čtvrtek', 'pátek', 'sobota', 'neděle'],									#CZ, Czech
	['montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag'],						#DE, German
	['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag'],								#DK, Danish
	['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],							#EN, English
	['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'],								#ES, Spanish
	['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai'],				#FI, Finnish
	['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'],								#FR, French
	['mánudagur', 'þriðjudagur', 'miðvikudagur', 'fimmtudagur', 'föstudagur', 'laugardagur', 'sunnudagur'],	#IS, Icelandic
	['δευτέρα', 'τρίτη', 'τετάρτη', 'πέμπτη', 'παρασκευή', 'σάββατο', 'κυριακή'],							#GR, Greek
	['hétfő', 'kedd', 'szerda', 'csütörtök', 'péntek', 'szombat', 'vasárnap'],								#HU, Hungarian
	['lunedì', 'martedì', 'mercoledì', 'giovedì', 'venerdì', 'sabato', 'domenica'],							#IT, Italian
	['maandag', 'dinsdag', 'woensdag', 'donderdag', 'vrijdag', 'zaterdag', 'zondag'],						#NL, Dutch
	['thứ hai', 'thứ ba', 'thứ tư', 'thứ năm', 'thứ sáu', 'thứ bảy', 'chủ nhật'],							#VI, Vietnamese
	['poniedziałek', 'wtorek', 'środa', 'czwartek', 'piątek', 'sobota', 'niedziela'],						#PL, Polish
	['luni', 'marţi', 'miercuri', 'joi', 'vineri', 'sâmbătă', 'duminică'],									#RO, Romanian
	['понедельник', 'вторник', 'среда', 'четверг', 'пятница', 'суббота', 'воскресенье'],						#RU, Russian
	['måndag', 'tisdag', 'onsdag', 'torsdag', 'fredag', 'lördag', 'söndag'],								#SE, Swedish
	['ponedeljek', 'torek', 'sreda', 'četrtek', 'petek', 'sobota', 'nedelja'],								#SI, Slovenian
	['pondelok', 'utorok', 'streda', 'štvrtok', 'piatok', 'sobota', 'nedeľa']								#SK, Slovak
]

#https://en.wiktionary.org/wiki/Appendix:Days_of_the_week 
#some of those are wrong jesus this took so long to find which characters were not exactly right

daysMonthNormalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

daysMonthLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

def getDayOfWeek(myDay, myMonth, myYear): 	#remember to subtract 1 from day and month (march is 2, friday is 4, etc)
	outDay = 3								#1970-01-01
	for yearRange in range(1970, myYear):
		#print yearRange
		if yearRange % 4 == 0 and (yearRange % 100 != 0 or yearRange % 400 == 0):
			outDay += 2 				#2 day displacement on leap years
			#print 'leapy'
		else:
			outDay += 1					#1 day displacement on normal years
		outDay = outDay % 7
		#print outDay

	for monthRange in range(0, myMonth):

		if myYear % 4 == 0 and (myYear % 100 != 0 or myYear % 400 == 0):
			outDay += daysMonthLeapYear[monthRange]
		else:
			outDay += daysMonthNormalYear[monthRange]
		outDay = outDay % 7

	outDay += myDay
	outDay = outDay % 7

	return outDay


for i,line in enumerate(lines[1:]):
	myLanguage = line.partition(':')[2].replace('\n', '')
	#print myLanguage
	if line[4] == '-':
		currentYear = int(line.partition('-')[0])
		currentMonth = int(line.partition('-')[2].partition('-')[0])
		currentDay = int(line.partition('-')[2].partition('-')[2].partition(':')[0])
		#print currentYear
	else:
		currentDay = int(line.partition('-')[0])
		currentMonth = int(line.partition('-')[2].partition('-')[0])
		currentYear = int(line.partition('-')[2].partition('-')[2].partition(':')[0])
	
	if currentYear % 4 == 0 and (currentYear % 100 != 0 or currentYear % 400 == 0):
		isLeapYear = True
		#print isLeapYear
		#print currentYear
	else:
		isLeapYear = False
	
	#print currentDay
	if currentMonth > 12:
		outputFile.write('Case #' + str(i + 1) + ': INVALID_DATE')
		if (i != totalCases - 1):
			outputFile.write('\n')
		continue
	

	if isLeapYear:
		if daysMonthLeapYear[currentMonth - 1] < currentDay:
			outputFile.write('Case #' + str(i + 1) + ': INVALID_DATE')
			if (i != totalCases - 1):
				outputFile.write('\n')
			continue
	else:
		if daysMonthNormalYear[currentMonth - 1] < currentDay:
			outputFile.write('Case #' + str(i + 1) + ': INVALID_DATE')
			if (i != totalCases - 1):
				outputFile.write('\n')
			continue
	#if we got here the date is gucci

	if myLanguage not in languageCodes:
		outputFile.write('Case #' + str(i + 1) + ': INVALID_LANGUAGE')
		if (i != totalCases - 1):
			outputFile.write('\n')
		continue
	else:
		myLanguageIndex = languageCodes.index(myLanguage)
	#if we got here the date and the langauge are fine

	myDayIndex = getDayOfWeek(currentDay - 1, currentMonth -1, currentYear)
	outputFile.write('Case #' + str(i + 1) + ': ' + daysOfWeek[myLanguageIndex][myDayIndex]) 

	if (i != totalCases - 1):
		outputFile.write('\n')



#print getDayOfWeek(1,11,2020)
