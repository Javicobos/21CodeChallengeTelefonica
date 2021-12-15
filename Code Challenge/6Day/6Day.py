# -*- coding: utf-8 -*-
lines = []
with open('testInput.txt', 'r') as f:
	lines = f.readlines()

outputFile = open('testOutput.txt', 'w')

totalCases = int(lines[0])


languageCodes = ['CA', 'CZ', 'DE', 'DK', 'EN', 'ES', 'FI', 'FR', 'IS', 'GR',
	'HU', 'IT', 'NL', 'VI', 'PL', 'RO', 'RU', 'SE', 'SI', 'SK']

daysOfWeek = [
	['dilluns', 'dimarts', 'dimecres', 'dijous', 'divendres', 'dissabte', 'diumenge'],						#CA, Catalan
	['pondělí', 'úterý', 'středu', 'čtvrtek', 'pátek', 'sobotu', 'neděli'],									#CZ, Czech
	['montag', 'dienstag', 'mittwoch', 'donnerstag', 'freitag', 'samstag', 'sonntag'],						#DE, German
	['mandag', 'tirsdag', 'onsdag', 'torsdag', 'fredag', 'lørdag', 'søndag'],								#DK, Danish
	['monday', 'tuesday', 'wednesday', 'thursday', 'friday', 'saturday', 'sunday'],							#EN, English
	['lunes', 'martes', 'miércoles', 'jueves', 'viernes', 'sábado', 'domingo'],								#ES, Spanish
	['maanantai', 'tiistai', 'keskiviikko', 'torstai', 'perjantai', 'lauantai', 'sunnuntai'],				#FI, Finnish
	['lundi', 'mardi', 'mercredi', 'jeudi', 'vendredi', 'samedi', 'dimanche'],								#FR, French
	['mánudagur', 'þriðjudagur', 'miðvikudagur', 'fimmtudagur', 'föstudagur', 'laugardagur', 'sunnudagur'],	#IS, Icelandic
	['δευτέρα', 'τρίτη', 'τετάρτη ', 'πέμπτη', 'παρασκευή', 'σάββατο', 'κυριακή'],							#GR, Greek
	['', '', '', '', '', '', ''],	#HU, Hungarian
	['', '', '', '', '', '', ''],	#IT, Italian
	['', '', '', '', '', '', ''],	#NL, Dutch
	['', '', '', '', '', '', ''],	#VI, Vietnamese
	['', '', '', '', '', '', ''],	#PL, Polish
	['', '', '', '', '', '', ''],	#RO, Romanian
	['', '', '', '', '', '', ''],	#RU, Russian 
	['', '', '', '', '', '', ''],	#SE, Swedish
	['', '', '', '', '', '', ''],	#SI, Slovenian
	['', '', '', '', '', '', '']	#SK, Slovak
]

#https://en.wiktionary.org/wiki/Appendix:Days_of_the_week

daysMonthNormalYear = [31, 28, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

daysMonthLeapYear = [31, 29, 31, 30, 31, 30, 31, 31, 30, 31, 30, 31]

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
	
	if currentYear % 4 == 0:
		if currentYear % 100 != 0 or currentYear % 400 == 0:
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


	if (i != totalCases - 1):
		outputFile.write('\n')

