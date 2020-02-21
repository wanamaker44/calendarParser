from dateutil.parser import parse
from datetime import datetime, timedelta

finalCsvOutput = 'Subject,Start Date, Start Time,End Date, End Time\n'

with open('games_to_import.csv','a') as fd:
	fd.write(finalCsvOutput)

inputString = "             1	Mon	22-Apr	Cypress Playground	9:00 PM	Wolf & Co	vs	Highrock\
             2	Wed	24-Apr	Cypress Playground	6:30 PM	SoBro Bulldogs	vs	Highrock\
             3	Tue	30-Apr	Brookline Avenue	6:30 PM	T's Pub	vs	Highrock\
             3	Tue	30-Apr	Brookline Avenue	7:45 PM	Bombers	vs	Highrock\
             4	Thurs	2-May	Brookline Avenue	6:30 PM	Highrock	vs	Dead Presidents\
             5	Mon	6-May	Cypress Playground	7:45 PM	Highrock	vs	Moe's Tavern \
             6	Thurs	9-May	Brookline Avenue	6:30 PM	Highrock	vs	Great Richards\
             7	Mon	13-May	Cypress Playground	6:30 PM	Cheryl Ann's Bakery	vs	Highrock\
             8	Wed	15-May	Brookline Avenue	7:45 PM	Highrock	vs	O'Leary's Pub \
             9	Tue	21-May	Brookline Avenue	6:30 PM	Golden's Garage	vs	Highrock\
             9	Tue	21-May	Brookline Avenue	7:45 PM	Highrock	vs	Clients \
           10	Wed	22-May	Cypress Playground	6:30 PM	Highrock	vs	Hamilton Restaurant & Bar \
           10	Wed	22-May	Cypress Playground	7:45 PM	Highrock	vs	Grainne O'Malley's Tavern\
           12	Wed	29-May	Cypress Playground	6:30 PM	Chestnut Hill Realty 	vs	Highrock"

inputLines = inputString.split('\n')

for indLine in inputLines:

	inputArray = indLine.split('\t')
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
			#print(gameJSON)
			print()

			newEvent = (summary + ',' + str(fullFinal.date()) + 
				',' + str(fullFinal.time()) + ',' + str(fullFinal.date()) + ',' +
				 str(finalEndTime.time()) + '\n')

			with open('games_to_import.csv','a') as fd:
				fd.write(newEvent)