from dateutil.parser import parse

inputString = '             3	Tue	30-Apr	Brookline Avenue	6:30 PM	T\'s Pub	vs	Highrock'
inputArray = inputString.split('\t')
description = ''
loopCounter = 0
finalOutDate = ''
finalOutTime = ''

for token in inputArray:
	token = token.strip()
	try:
		if(len(token) > 4):
			outDate = parse(token)
			if('pm' in token.lower()):
				finalOutTime = outDate.strftime('%H:%M')
			else:
				finalOutDate = outDate.strftime('%Y-%m-%d')
	except ValueError:
		description = description + str(token) + ' '
	loopCounter = loopCounter + 1
	if(loopCounter == len(inputArray)):
		print(finalOutDate, ' ', finalOutTime, ' ', description)