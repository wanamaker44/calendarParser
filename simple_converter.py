from dateutil.parser import parse
from datetime import datetime, timedelta

finalCsvOutput = 'Subject,Start Date, Start Time,End Date, End Time\n'

inputString = '             3	Tue	30-Apr	Brookline Avenue	6:30 PM	T\'s Pub	vs	Highrock'
inputArray = inputString.split('\t')
summary = ''
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
		summary = summary + str(token) + ' '
	loopCounter = loopCounter + 1
	if(loopCounter == len(inputArray)):
		fullFinal = datetime.strptime(finalOutDate+' '+finalOutTime+'-04:00', '%Y-%m-%d %H:%M%z')
		finalEndTime = fullFinal + timedelta(hours=1.5)
		gameJSON = {
			"start": {
				"dateTime": fullFinal.isoformat()
			},
			"end": {
				"dateTime": finalEndTime.isoformat()
			},
			"summary": summary
		}
		print(gameJSON)
		print()

		newEvent = (summary + ',' + str(fullFinal.date()) + 
			',' + str(fullFinal.time()) + ',' + str(fullFinal.date()) + ',' +
			 str(finalEndTime.time()) + '\n')
		finalCsvOutput = finalCsvOutput + newEvent

		print(finalCsvOutput)

with open('games_to_import.csv','a') as fd:
			fd.write(finalCsvOutput)